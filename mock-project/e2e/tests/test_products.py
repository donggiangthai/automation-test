"""
Products Page Tests.

These tests verify the products page functionality including:
- Viewing products
- Selecting cells
- Editing cells
- Saving changes

Trainees: This file contains mostly TODO tests for you to implement.
Use the examples in test_auth.py as reference.
"""

import pytest
from playwright.sync_api import Page, expect
from pages import ProductsPage


class TestProductsPageLoad:
    """Test suite for products page loading."""
    
    @pytest.mark.products
    @pytest.mark.smoke
    def test_products_page_loads(self, authenticated_page: Page):
        """
        Test that products page loads correctly.
        
        GIVEN: A user is authenticated
        WHEN: They navigate to the products page
        THEN: They should see the products table
        """
        products_page = ProductsPage(authenticated_page)
        products_page.navigate()
        
        products_page.assert_on_products_page()
        products_page.assert_table_has_data()
    
    @pytest.mark.products
    def test_products_page_shows_correct_title(self, authenticated_page: Page):
        """
        Test products page has correct title.
        
        TODO: Trainee should implement this test
        """
        # GIVEN: User is authenticated
        # WHEN: They navigate to products page
        # THEN: Page title should be "Products"
        pass
    
    @pytest.mark.products
    def test_products_table_has_correct_columns(self, authenticated_page: Page):
        """
        Test that products table has all expected columns.
        
        TODO: Trainee should implement this test
        """
        # Expected columns: ID, Product Name, SKU, Price, Category, Description
        # Hint: Use products_page.get_header() to check each column
        pass


class TestProductsCellSelection:
    """Test suite for cell selection functionality."""
    
    @pytest.mark.products
    def test_single_cell_selection(self, authenticated_page: Page):
        """
        Test that clicking a cell selects it.
        
        GIVEN: User is on products page
        WHEN: They click on a cell
        THEN: The cell should be selected
        AND: Selected count should show "1 cell(s) selected"
        """
        products_page = ProductsPage(authenticated_page)
        products_page.navigate()
        
        # Select a cell
        products_page.select_cell(1, "name")
        
        # Assert cell is selected
        products_page.assert_cell_selected(1, "name")
        
        # TODO: Assert selected count shows correct number
    
    @pytest.mark.products
    def test_multi_cell_selection_with_ctrl(self, authenticated_page: Page):
        """
        Test that Ctrl+click adds cells to selection.
        
        TODO: Trainee should implement this test
        """
        # GIVEN: User is on products page with one cell selected
        # WHEN: They Ctrl+click another cell
        # THEN: Both cells should be selected
        # AND: Selected count should show "2 cell(s) selected"
        pass
    
    @pytest.mark.products
    def test_clicking_new_cell_clears_previous_selection(
        self, authenticated_page: Page
    ):
        """
        Test that clicking without Ctrl clears previous selection.
        
        TODO: Trainee should implement this test
        """
        # GIVEN: User has selected a cell
        # WHEN: They click another cell (without Ctrl)
        # THEN: Only the new cell should be selected
        pass


class TestProductsCellEditing:
    """Test suite for cell editing functionality."""
    
    @pytest.mark.products
    def test_double_click_enables_edit_mode(self, authenticated_page: Page):
        """
        Test that double-clicking a cell enters edit mode.
        
        TODO: Trainee should implement this test
        """
        # GIVEN: User is on products page
        # WHEN: They double-click a cell
        # THEN: An input field should appear
        pass
    
    @pytest.mark.products
    def test_edit_cell_value(self, authenticated_page: Page):
        """
        Test editing a cell value.
        
        GIVEN: User is on products page
        WHEN: They edit a cell value
        THEN: The cell should show the new value
        AND: Pending changes count should increase
        """
        products_page = ProductsPage(authenticated_page)
        products_page.navigate()
        
        # Edit a cell
        products_page.edit_cell(1, "name", "New Product Name")
        
        # Assert the value changed
        products_page.assert_cell_value(1, "name", "New Product Name")
        
        # Assert cell is marked as modified
        products_page.assert_cell_modified(1, "name")
    
    @pytest.mark.products
    def test_edit_number_cell(self, authenticated_page: Page):
        """
        Test editing a number cell (price).
        
        TODO: Trainee should implement this test
        """
        # GIVEN: User is on products page
        # WHEN: They edit the price cell
        # THEN: The new price should be displayed
        pass
    
    @pytest.mark.products
    def test_escape_cancels_edit(self, authenticated_page: Page):
        """
        Test that pressing Escape cancels cell editing.
        
        TODO: Trainee should implement this test
        """
        # GIVEN: User is editing a cell
        # WHEN: They press Escape
        # THEN: Edit mode should be cancelled
        # AND: Original value should be preserved
        pass


class TestProductsSaveReset:
    """Test suite for save and reset functionality."""
    
    @pytest.mark.products
    def test_save_button_disabled_when_no_changes(
        self, authenticated_page: Page
    ):
        """
        Test save button is disabled when no changes.
        
        GIVEN: User is on products page
        WHEN: No changes have been made
        THEN: Save button should be disabled
        """
        products_page = ProductsPage(authenticated_page)
        products_page.navigate()
        
        products_page.assert_save_button_disabled()
    
    @pytest.mark.products
    def test_save_button_enabled_after_edit(self, authenticated_page: Page):
        """
        Test save button is enabled after making changes.
        
        TODO: Trainee should implement this test
        """
        # GIVEN: User is on products page
        # WHEN: They edit a cell
        # THEN: Save button should be enabled
        pass
    
    @pytest.mark.products
    def test_save_persists_changes(self, authenticated_page: Page):
        """
        Test that saving changes persists them.
        
        TODO: Trainee should implement this test
        """
        # GIVEN: User has made changes to a cell
        # WHEN: They click save
        # THEN: Changes should persist after page reload
        pass
    
    @pytest.mark.products
    def test_reset_discards_changes(self, authenticated_page: Page):
        """
        Test that reset discards all pending changes.
        
        TODO: Trainee should implement this test
        """
        # GIVEN: User has made changes to cells
        # WHEN: They click reset
        # THEN: All changes should be discarded
        # AND: Original values should be restored
        # AND: Save button should be disabled
        pass


class TestProductsEdgeCases:
    """Test suite for edge cases and error handling."""
    
    @pytest.mark.products
    def test_cannot_edit_id_column(self, authenticated_page: Page):
        """
        Test that ID column cannot be edited.
        
        TODO: Trainee should implement this test
        """
        # GIVEN: User is on products page
        # WHEN: They try to edit the ID column
        # THEN: No edit input should appear
        pass
    
    @pytest.mark.products
    @pytest.mark.slow
    def test_bulk_edit_multiple_cells(self, authenticated_page: Page):
        """
        Test editing multiple cells and saving.
        
        TODO: Trainee should implement this test
        """
        # GIVEN: User is on products page
        # WHEN: They edit multiple cells (name, price, category)
        # THEN: All changes should be saved correctly
        pass
