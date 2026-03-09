"""
Products Page Object.

Represents the Products page with editable table functionality.

TODO: Trainee should complete the implementation of this Page Object.
Study the existing methods and implement the TODOs.
"""

from playwright.sync_api import Page, Locator, expect
from .base_page import BasePage


class ProductsPage(BasePage):
    """
    Page Object for the Products page.
    
    Provides methods to:
    - View and navigate products table
    - Select cells (single and multi-select)
    - Edit cell values
    - Save and reset changes
    
    Trainees: Complete the TODO sections to practice
    implementing Page Object methods.
    """
    
    PATH = "/products"
    TABLE_NAME = "products"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    # ==========================================================================
    # Navigation
    # ==========================================================================
    
    def navigate(self) -> "ProductsPage":
        """Navigate to products page."""
        self.goto(self.PATH)
        self.wait_for_table_load()
        return self
    
    # ==========================================================================
    # Table Locators
    # ==========================================================================
    
    @property
    def table(self) -> Locator:
        """Get products table element."""
        return self.page.locator(f'[data-testid="{self.TABLE_NAME}-table"]')
    
    @property
    def page_title(self) -> Locator:
        """Get page title."""
        return self.page.locator('[data-testid="page-title"]')
    
    @property
    def save_button(self) -> Locator:
        """Get save button."""
        return self.page.locator('[data-testid="save-button"]')
    
    @property
    def reset_button(self) -> Locator:
        """Get reset button."""
        return self.page.locator('[data-testid="reset-button"]')
    
    @property
    def selected_count(self) -> Locator:
        """Get selected cells count indicator."""
        return self.page.locator('[data-testid="selected-count"]')
    
    @property
    def pending_count(self) -> Locator:
        """Get pending changes count indicator."""
        return self.page.locator('[data-testid="pending-count"]')
    
    @property
    def empty_state(self) -> Locator:
        """Get empty state message."""
        return self.page.locator('[data-testid="empty-state"]')
    
    # ==========================================================================
    # Table Helpers
    # ==========================================================================
    
    def get_row(self, row_id: int) -> Locator:
        """
        Get a specific row by ID.
        
        Args:
            row_id: The ID of the row (product ID)
        
        Returns:
            Locator for the row
        """
        return self.page.locator(f'[data-testid="row-{row_id}"]')
    
    def get_cell(self, row_id: int, column_key: str) -> Locator:
        """
        Get a specific cell.
        
        Args:
            row_id: The ID of the row
            column_key: The column key (e.g., "name", "price")
        
        Returns:
            Locator for the cell
        """
        return self.page.locator(
            f'[data-testid="cell-{row_id}-{column_key}"]'
        )
    
    def get_cell_value(self, row_id: int, column_key: str) -> Locator:
        """
        Get the value display element of a cell.
        
        Args:
            row_id: The ID of the row
            column_key: The column key
        
        Returns:
            Locator for the value element
        """
        return self.page.locator(
            f'[data-testid="value-{row_id}-{column_key}"]'
        )
    
    def get_cell_input(self, row_id: int, column_key: str) -> Locator:
        """
        Get the input element of a cell (when editing).
        
        Args:
            row_id: The ID of the row
            column_key: The column key
        
        Returns:
            Locator for the input element
        """
        return self.page.locator(
            f'[data-testid="input-{row_id}-{column_key}"]'
        )
    
    def get_header(self, column_key: str) -> Locator:
        """
        Get a column header.
        
        Args:
            column_key: The column key
        
        Returns:
            Locator for the header
        """
        return self.page.locator(f'[data-testid="header-{column_key}"]')
    
    # ==========================================================================
    # Cell Selection
    # ==========================================================================
    
    def select_cell(self, row_id: int, column_key: str) -> None:
        """
        Select a single cell (clears other selections).
        
        Args:
            row_id: The ID of the row
            column_key: The column key
        """
        cell = self.get_cell(row_id, column_key)
        cell.click()
    
    def multi_select_cell(self, row_id: int, column_key: str) -> None:
        """
        Add a cell to the current selection (Ctrl/Cmd + click).
        
        Args:
            row_id: The ID of the row
            column_key: The column key
        """
        cell = self.get_cell(row_id, column_key)
        # Use keyboard modifier for multi-select
        cell.click(modifiers=["Control"])  # Use "Meta" for Mac
    
    def get_selected_count(self) -> int:
        """
        Get the number of selected cells.
        
        Returns:
            Number of selected cells, or 0 if none selected
        """
        # TODO: Trainee should implement this
        # Hint: Parse the text from selected_count locator
        # Example text: "3 cell(s) selected"
        pass
    
    # ==========================================================================
    # Cell Editing
    # ==========================================================================
    
    def edit_cell(self, row_id: int, column_key: str, value: str) -> None:
        """
        Edit a cell value.
        
        Double-clicks to enter edit mode, types the value,
        and presses Enter to confirm.
        
        Args:
            row_id: The ID of the row
            column_key: The column key
            value: The new value to enter
        """
        # Double-click to enter edit mode
        cell = self.get_cell(row_id, column_key)
        cell.dblclick()
        
        # Clear existing value and type new one
        input_element = self.get_cell_input(row_id, column_key)
        input_element.fill(value)
        
        # Press Enter to confirm
        input_element.press("Enter")
    
    def get_pending_changes_count(self) -> int:
        """
        Get the number of pending (unsaved) changes.
        
        Returns:
            Number of pending changes, or 0 if none
        """
        # TODO: Trainee should implement this
        # Hint: Parse the text from pending_count locator
        # Example text: "5 pending change(s)"
        pass
    
    # ==========================================================================
    # Actions
    # ==========================================================================
    
    def save_changes(self) -> None:
        """
        Click the save button to persist changes.
        
        Waits for the save operation to complete.
        """
        self.save_button.click()
        # Wait for button to be re-enabled (save complete)
        self.page.wait_for_function(
            '() => !document.querySelector("[data-testid=save-button]").disabled'
        )
    
    def reset_changes(self) -> None:
        """
        Click the reset button to discard all changes.
        """
        self.reset_button.click()
    
    def wait_for_table_load(self) -> None:
        """Wait for the table to be loaded and visible."""
        self.table.wait_for(state="visible")
    
    # ==========================================================================
    # Assertions
    # ==========================================================================
    
    def assert_on_products_page(self) -> None:
        """Assert we are on the products page."""
        expect(self.page).to_have_url("**/products")
        expect(self.page_title).to_have_text("Products")
    
    def assert_cell_value(
        self, row_id: int, column_key: str, expected_value: str
    ) -> None:
        """
        Assert a cell has the expected value.
        
        Args:
            row_id: The ID of the row
            column_key: The column key
            expected_value: Expected cell value
        """
        cell_value = self.get_cell_value(row_id, column_key)
        expect(cell_value).to_have_text(expected_value)
    
    def assert_cell_selected(self, row_id: int, column_key: str) -> None:
        """
        Assert a cell is selected.
        
        Args:
            row_id: The ID of the row
            column_key: The column key
        """
        # TODO: Trainee should implement this
        # Hint: Check if the cell has the selected styling (ring-2 class)
        pass
    
    def assert_cell_modified(self, row_id: int, column_key: str) -> None:
        """
        Assert a cell has been modified (pending change).
        
        Args:
            row_id: The ID of the row
            column_key: The column key
        """
        # TODO: Trainee should implement this
        # Hint: Check if the cell has the modified styling (bg-yellow-50)
        pass
    
    def assert_save_button_enabled(self) -> None:
        """Assert save button is enabled."""
        expect(self.save_button).to_be_enabled()
    
    def assert_save_button_disabled(self) -> None:
        """Assert save button is disabled."""
        expect(self.save_button).to_be_disabled()
    
    def assert_table_has_data(self) -> None:
        """Assert table has at least one row of data."""
        expect(self.table.locator("tbody tr").first).to_be_visible()
    
    def assert_table_empty(self) -> None:
        """Assert table is empty (shows empty state)."""
        expect(self.empty_state).to_be_visible()
