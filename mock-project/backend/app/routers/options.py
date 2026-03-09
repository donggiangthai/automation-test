"""
Options/Lookups API Routes
Provides dropdown options for UI components
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import distinct

from app.database import get_db
from app.models import Product, Inventory, OrderStatus

router = APIRouter()


@router.get("/categories")
async def get_categories(db: Session = Depends(get_db)):
    """Get unique product categories"""
    categories = db.query(distinct(Product.category)).filter(
        Product.category.isnot(None)
    ).all()
    return [cat[0] for cat in categories if cat[0]]


@router.get("/locations")
async def get_locations(db: Session = Depends(get_db)):
    """Get unique inventory locations"""
    locations = db.query(distinct(Inventory.location)).filter(
        Inventory.location.isnot(None)
    ).all()
    return [loc[0] for loc in locations if loc[0]]


@router.get("/order-statuses")
async def get_order_statuses():
    """Get available order statuses"""
    return [status.value for status in OrderStatus]


@router.get("/all")
async def get_all_options(db: Session = Depends(get_db)):
    """Get all dropdown options in one call"""
    categories = db.query(distinct(Product.category)).filter(
        Product.category.isnot(None)
    ).all()
    
    locations = db.query(distinct(Inventory.location)).filter(
        Inventory.location.isnot(None)
    ).all()
    
    return {
        "categories": [cat[0] for cat in categories if cat[0]],
        "locations": [loc[0] for loc in locations if loc[0]],
        "orderStatuses": [status.value for status in OrderStatus]
    }
