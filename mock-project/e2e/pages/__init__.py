# Page Objects module
from .base_page import BasePage
from .login_page import LoginPage
from .products_page import ProductsPage
from .inventory_page import InventoryPage
from .orders_page import OrdersPage

__all__ = [
    "BasePage",
    "LoginPage",
    "ProductsPage",
    "InventoryPage",
    "OrdersPage",
]
