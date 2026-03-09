"""
Products router - CRUD operations for products
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import Product, User
from app.schemas import (
    ProductResponse, 
    ProductCreate, 
    ProductUpdate, 
    ProductBulkUpdate,
    BulkUpdateResponse
)
from app.routers.auth import get_current_user

router = APIRouter()


@router.get("", response_model=List[ProductResponse])
async def list_products(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all products"""
    products = db.query(Product).offset(skip).limit(limit).all()
    return products


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a specific product"""
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("", response_model=ProductResponse)
async def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new product"""
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update a product"""
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    update_data = product.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_product, field, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product


@router.patch("/bulk", response_model=BulkUpdateResponse)
async def bulk_update_products(
    updates: List[ProductBulkUpdate],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Bulk update multiple products"""
    updated_count = 0
    
    for update in updates:
        product = db.query(Product).filter(Product.id == update.id).first()
        if product:
            update_data = update.model_dump(exclude_unset=True, exclude={'id'})
            for field, value in update_data.items():
                if value is not None:
                    setattr(product, field, value)
            updated_count += 1
    
    db.commit()
    return BulkUpdateResponse(
        updated=updated_count,
        message=f"Successfully updated {updated_count} products"
    )


@router.delete("/{product_id}")
async def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a product"""
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}
