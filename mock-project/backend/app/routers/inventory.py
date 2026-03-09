"""
Inventory router - Stock management
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import Inventory, Product, User
from app.schemas import (
    InventoryResponse,
    InventoryUpdate,
    InventoryBulkUpdate,
    BulkUpdateResponse
)
from app.routers.auth import get_current_user

router = APIRouter()


@router.get("", response_model=List[InventoryResponse])
async def list_inventory(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all inventory items"""
    inventory_items = db.query(Inventory).offset(skip).limit(limit).all()
    
    # Add product name to response
    result = []
    for item in inventory_items:
        item_dict = {
            "id": item.id,
            "product_id": item.product_id,
            "quantity": item.quantity,
            "min_quantity": item.min_quantity,
            "location": item.location,
            "updated_at": item.updated_at,
            "product_name": item.product.name if item.product else None
        }
        result.append(item_dict)
    
    return result


@router.get("/{inventory_id}", response_model=InventoryResponse)
async def get_inventory_item(
    inventory_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a specific inventory item"""
    item = db.query(Inventory).filter(Inventory.id == inventory_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    
    return {
        "id": item.id,
        "product_id": item.product_id,
        "quantity": item.quantity,
        "min_quantity": item.min_quantity,
        "location": item.location,
        "updated_at": item.updated_at,
        "product_name": item.product.name if item.product else None
    }


@router.put("/{inventory_id}", response_model=InventoryResponse)
async def update_inventory(
    inventory_id: int,
    inventory: InventoryUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update an inventory item"""
    db_item = db.query(Inventory).filter(Inventory.id == inventory_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    
    update_data = inventory.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_item, field, value)
    
    db.commit()
    db.refresh(db_item)
    
    return {
        "id": db_item.id,
        "product_id": db_item.product_id,
        "quantity": db_item.quantity,
        "min_quantity": db_item.min_quantity,
        "location": db_item.location,
        "updated_at": db_item.updated_at,
        "product_name": db_item.product.name if db_item.product else None
    }


@router.patch("/bulk", response_model=BulkUpdateResponse)
async def bulk_update_inventory(
    updates: List[InventoryBulkUpdate],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Bulk update multiple inventory items"""
    updated_count = 0
    
    for update in updates:
        item = db.query(Inventory).filter(Inventory.id == update.id).first()
        if item:
            update_data = update.model_dump(exclude_unset=True, exclude={'id'})
            for field, value in update_data.items():
                if value is not None:
                    setattr(item, field, value)
            updated_count += 1
    
    db.commit()
    return BulkUpdateResponse(
        updated=updated_count,
        message=f"Successfully updated {updated_count} inventory items"
    )
