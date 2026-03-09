"""
Pydantic schemas for request/response validation
"""
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


# ============ User Schemas ============

class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    picture: Optional[str] = None


class UserResponse(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse


# ============ Product Schemas ============

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category: Optional[str] = None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None


class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class ProductBulkUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None


# ============ Inventory Schemas ============

class InventoryBase(BaseModel):
    quantity: int
    min_quantity: int = 10
    location: Optional[str] = None


class InventoryUpdate(BaseModel):
    quantity: Optional[int] = None
    min_quantity: Optional[int] = None
    location: Optional[str] = None


class InventoryResponse(InventoryBase):
    id: int
    product_id: int
    product_name: Optional[str] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class InventoryBulkUpdate(BaseModel):
    id: int
    quantity: Optional[int] = None
    min_quantity: Optional[int] = None
    location: Optional[str] = None


# ============ Order Schemas ============

class OrderBase(BaseModel):
    customer_name: str
    customer_email: EmailStr
    product_id: int
    quantity: int
    total_amount: float
    status: str = "pending"
    notes: Optional[str] = None


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    customer_email: Optional[EmailStr] = None
    quantity: Optional[int] = None
    total_amount: Optional[float] = None
    status: Optional[str] = None
    notes: Optional[str] = None


class OrderResponse(OrderBase):
    id: int
    product_name: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class OrderBulkUpdate(BaseModel):
    id: int
    customer_name: Optional[str] = None
    customer_email: Optional[str] = None
    quantity: Optional[int] = None
    total_amount: Optional[float] = None
    status: Optional[str] = None
    notes: Optional[str] = None


# ============ Generic Schemas ============

class BulkUpdateRequest(BaseModel):
    items: List[dict]


class BulkUpdateResponse(BaseModel):
    updated: int
    message: str
