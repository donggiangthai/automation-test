"""
Orders router - Order management
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import Order, User
from app.schemas import (
    OrderResponse,
    OrderBase,
    OrderUpdate,
    OrderBulkUpdate,
    BulkUpdateResponse
)
from app.routers.auth import get_current_user

router = APIRouter()


@router.get("", response_model=List[OrderResponse])
async def list_orders(
    skip: int = 0,
    limit: int = 100,
    status: str = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all orders"""
    query = db.query(Order)
    
    if status:
        query = query.filter(Order.status == status)
    
    orders = query.offset(skip).limit(limit).all()
    
    # Add product name to response
    result = []
    for order in orders:
        order_dict = {
            "id": order.id,
            "customer_name": order.customer_name,
            "customer_email": order.customer_email,
            "product_id": order.product_id,
            "quantity": order.quantity,
            "total_amount": order.total_amount,
            "status": order.status,
            "notes": order.notes,
            "created_at": order.created_at,
            "updated_at": order.updated_at,
            "product_name": order.product.name if order.product else None
        }
        result.append(order_dict)
    
    return result


@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a specific order"""
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    return {
        "id": order.id,
        "customer_name": order.customer_name,
        "customer_email": order.customer_email,
        "product_id": order.product_id,
        "quantity": order.quantity,
        "total_amount": order.total_amount,
        "status": order.status,
        "notes": order.notes,
        "created_at": order.created_at,
        "updated_at": order.updated_at,
        "product_name": order.product.name if order.product else None
    }


@router.post("", response_model=OrderResponse)
async def create_order(
    order: OrderBase,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new order"""
    db_order = Order(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    
    return {
        "id": db_order.id,
        "customer_name": db_order.customer_name,
        "customer_email": db_order.customer_email,
        "product_id": db_order.product_id,
        "quantity": db_order.quantity,
        "total_amount": db_order.total_amount,
        "status": db_order.status,
        "notes": db_order.notes,
        "created_at": db_order.created_at,
        "updated_at": db_order.updated_at,
        "product_name": db_order.product.name if db_order.product else None
    }


@router.put("/{order_id}", response_model=OrderResponse)
async def update_order(
    order_id: int,
    order: OrderUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update an order"""
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    update_data = order.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_order, field, value)
    
    db.commit()
    db.refresh(db_order)
    
    return {
        "id": db_order.id,
        "customer_name": db_order.customer_name,
        "customer_email": db_order.customer_email,
        "product_id": db_order.product_id,
        "quantity": db_order.quantity,
        "total_amount": db_order.total_amount,
        "status": db_order.status,
        "notes": db_order.notes,
        "created_at": db_order.created_at,
        "updated_at": db_order.updated_at,
        "product_name": db_order.product.name if db_order.product else None
    }


@router.patch("/bulk", response_model=BulkUpdateResponse)
async def bulk_update_orders(
    updates: List[OrderBulkUpdate],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Bulk update multiple orders"""
    updated_count = 0
    
    for update in updates:
        order = db.query(Order).filter(Order.id == update.id).first()
        if order:
            update_data = update.model_dump(exclude_unset=True, exclude={'id'})
            for field, value in update_data.items():
                if value is not None:
                    setattr(order, field, value)
            updated_count += 1
    
    db.commit()
    return BulkUpdateResponse(
        updated=updated_count,
        message=f"Successfully updated {updated_count} orders"
    )


@router.delete("/{order_id}")
async def delete_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete an order"""
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    db.delete(order)
    db.commit()
    return {"message": "Order deleted successfully"}
