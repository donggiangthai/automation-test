"""
Orders Page Object.

TODO: Trainee should implement this Page Object.
Use ProductsPage as a reference for the pattern.
"""

from playwright.sync_api import Page, Locator, expect
from .base_page import BasePage


class OrdersPage(BasePage):
    """
    Page Object for the Orders page.
    
    TODO: Trainee should implement this class.
    
    The Orders page has similar functionality to Products:
    - Editable table with cells
    - Select, multi-select, edit cells
    - Save and reset buttons
    
    Additional features:
    - Status filter dropdown
    - Status badges showing count for each status
    
    Columns:
    - id (number, read-only)
    - customer_name (string, editable)
    - customer_email (string, editable)
    - status (string, editable - pending/processing/shipped/delivered/cancelled)
    - total_amount (number, editable)
    - shipping_address (string, editable)
    - created_at (string, read-only)
    """
    
    PATH = "/orders"
    TABLE_NAME = "orders"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    # ==========================================================================
    # TODO: Implement Navigation
    # ==========================================================================
    
    def navigate(self) -> "OrdersPage":
        """Navigate to orders page."""
        # TODO: Implement this method
        pass
    
    # ==========================================================================
    # Orders-Specific Locators
    # ==========================================================================
    
    @property
    def status_filter(self) -> Locator:
        """Get status filter dropdown."""
        return self.page.locator('[data-testid="status-filter"]')
    
    def get_status_badge(self, status: str) -> Locator:
        """
        Get status badge for a specific status.
        
        Args:
            status: Status name (e.g., "pending", "shipped")
        
        Returns:
            Locator for the status badge
        """
        return self.page.locator(f'[data-testid="status-badge-{status}"]')
    
    # ==========================================================================
    # Status Filter Actions
    # ==========================================================================
    
    def filter_by_status(self, status: str) -> None:
        """
        Filter orders by status.
        
        Args:
            status: Status to filter by ("all" for no filter)
        """
        self.status_filter.select_option(status)
    
    def clear_filter(self) -> None:
        """Clear status filter (show all orders)."""
        self.filter_by_status("all")
    
    def get_status_count(self, status: str) -> int:
        """
        Get count of orders with a specific status.
        
        Args:
            status: Status to count
        
        Returns:
            Number of orders with that status
        """
        # TODO: Trainee should implement this
        # Hint: Parse the text from status badge
        # Example text: "pending: 5"
        pass
    
    # ==========================================================================
    # TODO: Implement Table Locators
    # ==========================================================================
    
    @property
    def table(self) -> Locator:
        """Get orders table element."""
        # TODO: Implement this property
        pass
    
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
    
    def assert_on_orders_page(self) -> None:
        """Assert we are on the orders page."""
        # TODO: Implement this assertion
        pass
    
    def assert_filter_applied(self, status: str) -> None:
        """Assert filter is applied."""
        # TODO: Check that status_filter has the correct value selected
        pass
    
    # TODO: Add more assertions as needed
