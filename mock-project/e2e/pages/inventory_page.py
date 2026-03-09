"""
Inventory Page Object.

TODO: Trainee should implement this Page Object.
Use ProductsPage as a reference for the pattern.
"""

from playwright.sync_api import Page, Locator, expect
from .base_page import BasePage


class InventoryPage(BasePage):
    """
    Page Object for the Inventory page.
    
    TODO: Trainee should implement this class.
    
    The Inventory page has similar functionality to Products:
    - Editable table with cells
    - Select, multi-select, edit cells
    - Save and reset buttons
    
    Additional features:
    - Low stock warning indicator
    - Product name is read-only (from related product)
    
    Columns:
    - id (number, read-only)
    - product_name (string, read-only)
    - quantity (number, editable)
    - location (string, editable)
    - min_quantity (number, editable)
    - max_quantity (number, editable)
    - last_restocked (string, read-only)
    """
    
    PATH = "/inventory"
    TABLE_NAME = "inventory"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    # ==========================================================================
    # TODO: Implement Navigation
    # ==========================================================================
    
    def navigate(self) -> "InventoryPage":
        """Navigate to inventory page."""
        # TODO: Implement this method
        pass
    
    # ==========================================================================
    # TODO: Implement Table Locators
    # ==========================================================================
    
    @property
    def table(self) -> Locator:
        """Get inventory table element."""
        # TODO: Implement this property
        pass
    
    @property
    def low_stock_warning(self) -> Locator:
        """Get low stock warning element."""
        return self.page.locator('[data-testid="low-stock-warning"]')
    
    # TODO: Add more locators (save_button, reset_button, etc.)
    
    # ==========================================================================
    # TODO: Implement Table Helpers
    # ==========================================================================
    
    # Copy and adapt methods from ProductsPage:
    # - get_row()
    # - get_cell()
    # - get_cell_value()
    # - get_cell_input()
    
    # ==========================================================================
    # TODO: Implement Cell Selection & Editing
    # ==========================================================================
    
    # Copy and adapt methods from ProductsPage:
    # - select_cell()
    # - multi_select_cell()
    # - edit_cell()
    
    # ==========================================================================
    # TODO: Implement Actions
    # ==========================================================================
    
    # Copy and adapt methods from ProductsPage:
    # - save_changes()
    # - reset_changes()
    
    # ==========================================================================
    # TODO: Implement Assertions
    # ==========================================================================
    
    def assert_on_inventory_page(self) -> None:
        """Assert we are on the inventory page."""
        # TODO: Implement this assertion
        pass
    
    def assert_low_stock_warning_visible(self) -> None:
        """Assert low stock warning is displayed."""
        expect(self.low_stock_warning).to_be_visible()
    
    def assert_low_stock_warning_hidden(self) -> None:
        """Assert low stock warning is not displayed."""
        expect(self.low_stock_warning).not_to_be_visible()
    
    # TODO: Add more assertions as needed
