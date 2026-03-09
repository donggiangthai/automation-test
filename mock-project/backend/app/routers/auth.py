"""
Authentication router - Google SSO
"""
from fastapi import APIRouter, Depends, HTTPException, Response, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from authlib.integrations.starlette_client import OAuth
from jose import jwt
from datetime import datetime, timedelta
from typing import Optional

from app.database import get_db
from app.config import settings
from app.models import User
from app.schemas import UserResponse, TokenResponse

router = APIRouter()

# OAuth setup
oauth = OAuth()
oauth.register(
    name='google',
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'}
)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Create JWT access token"""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")


def get_current_user(request: Request, db: Session = Depends(get_db)) -> User:
    """Dependency to get current authenticated user"""
    # Check for bypass auth in development
    if settings.BYPASS_AUTH:
        user = db.query(User).filter(User.email == settings.TEST_USER_EMAIL).first()
        if not user:
            user = User(email=settings.TEST_USER_EMAIL, name="Test User")
            db.add(user)
            db.commit()
            db.refresh(user)
        return user
    
    # Check Authorization header
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    token = auth_header.split(" ")[1]
    
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=401, detail="Invalid token")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    
    return user


@router.get("/google")
async def google_login(request: Request):
    """Initiate Google OAuth login"""
    if settings.BYPASS_AUTH:
        # In bypass mode, redirect directly with test token
        return RedirectResponse(url=f"{settings.FRONTEND_URL}/auth/callback?bypass=true")
    
    redirect_uri = request.url_for('google_callback')
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/callback")
async def google_callback(request: Request, db: Session = Depends(get_db)):
    """Handle Google OAuth callback"""
    if settings.BYPASS_AUTH:
        # Create or get test user
        user = db.query(User).filter(User.email == settings.TEST_USER_EMAIL).first()
        if not user:
            user = User(
                email=settings.TEST_USER_EMAIL,
                name="Test User",
                picture=None
            )
            db.add(user)
            db.commit()
            db.refresh(user)
        
        token = create_access_token({"sub": user.email})
        return RedirectResponse(
            url=f"{settings.FRONTEND_URL}/auth/callback?token={token}"
        )
    
    try:
        token_data = await oauth.google.authorize_access_token(request)
        user_info = token_data.get('userinfo')
        
        if not user_info:
            raise HTTPException(status_code=400, detail="Failed to get user info")
        
        # Create or update user
        user = db.query(User).filter(User.email == user_info['email']).first()
        if not user:
            user = User(
                email=user_info['email'],
                name=user_info.get('name'),
                picture=user_info.get('picture')
            )
            db.add(user)
        else:
            user.name = user_info.get('name')
            user.picture = user_info.get('picture')
        
        db.commit()
        db.refresh(user)
        
        # Create JWT token
        access_token = create_access_token({"sub": user.email})
        
        # Redirect to frontend with token
        return RedirectResponse(
            url=f"{settings.FRONTEND_URL}/auth/callback?token={access_token}"
        )
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    """Get current user info"""
    return current_user


@router.post("/logout")
async def logout(response: Response):
    """Logout user"""
    response.delete_cookie("access_token")
    return {"message": "Logged out successfully"}


# Development endpoint for getting test token
@router.post("/dev-token", response_model=TokenResponse)
async def get_dev_token(db: Session = Depends(get_db)):
    """Get development token (only works when BYPASS_AUTH=true)"""
    if not settings.BYPASS_AUTH:
        raise HTTPException(status_code=403, detail="Not available in production")
    
    user = db.query(User).filter(User.email == settings.TEST_USER_EMAIL).first()
    if not user:
        user = User(email=settings.TEST_USER_EMAIL, name="Test User")
        db.add(user)
        db.commit()
        db.refresh(user)
    
    token = create_access_token({"sub": user.email})
    return TokenResponse(access_token=token, user=UserResponse.model_validate(user))
