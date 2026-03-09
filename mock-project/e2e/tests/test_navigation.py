"""
Navigation Tests.

Tests for sidebar navigation and page transitions.
"""

import pytest
from playwright.sync_api import Page, expect
from pages import BasePage, ProductsPage


class TestSidebarNavigation:
    """Test suite for sidebar navigation functionality."""
    
    @pytest.mark.navigation
    @pytest.mark.smoke
    def test_navigate_to_products(self, authenticated_page: Page):
        """
        Test navigating to products page via sidebar.
        
        GIVEN: User is authenticated
        WHEN: They click Products in the sidebar
        THEN: They should be on the products page
        """
        base_page = BasePage(authenticated_page)
        base_page.go_to_products()
        
        expect(authenticated_page).to_have_url("**/products")
    
    @pytest.mark.navigation
    @pytest.mark.smoke
    def test_navigate_to_inventory(self, authenticated_page: Page):
        """
        Test navigating to inventory page via sidebar.
        
        TODO: Trainee should implement this test
        """
        pass
    
    @pytest.mark.navigation
    @pytest.mark.smoke
    def test_navigate_to_orders(self, authenticated_page: Page):
        """
        Test navigating to orders page via sidebar.
        
        TODO: Trainee should implement this test
        """
        pass
    
    @pytest.mark.navigation
    def test_navigate_between_all_pages(self, authenticated_page: Page):
        """
        Test navigating between all pages in sequence.
        
        GIVEN: User is on products page
        WHEN: They navigate Products -> Inventory -> Orders -> Products
        THEN: Each navigation should succeed
        """
        base_page = BasePage(authenticated_page)
        
        # Start at products
        base_page.go_to_products()
        expect(authenticated_page).to_have_url("**/products")
        
        # Go to inventory
        base_page.go_to_inventory()
        expect(authenticated_page).to_have_url("**/inventory")
        
        # Go to orders
        base_page.go_to_orders()
        expect(authenticated_page).to_have_url("**/orders")
        
        # Back to products
        base_page.go_to_products()
        expect(authenticated_page).to_have_url("**/products")


class TestSidebarCollapse:
    """Test suite for sidebar collapse/expand functionality."""
    
    @pytest.mark.navigation
    def test_collapse_sidebar(self, authenticated_page: Page):
        """
        Test collapsing the sidebar.
        
        GIVEN: Sidebar is expanded
        WHEN: User clicks collapse button
        THEN: Sidebar should be collapsed
        """
        base_page = BasePage(authenticated_page)
        base_page.go_to_products()
        
        # Ensure sidebar is expanded
        base_page.expand_sidebar()
        assert not base_page.is_sidebar_collapsed()
        
        # Collapse sidebar
        base_page.collapse_sidebar()
        assert base_page.is_sidebar_collapsed()
    
    @pytest.mark.navigation
    def test_expand_sidebar(self, authenticated_page: Page):
        """
        Test expanding the sidebar.
        
        TODO: Trainee should implement this test
        """
        # GIVEN: Sidebar is collapsed
        # WHEN: User clicks expand button
        # THEN: Sidebar should be expanded
        pass
    
    @pytest.mark.navigation
    def test_navigation_works_when_collapsed(self, authenticated_page: Page):
        """
        Test that navigation still works when sidebar is collapsed.
        
        TODO: Trainee should implement this test
        """
        # GIVEN: Sidebar is collapsed
        # WHEN: User clicks navigation icons
        # THEN: Navigation should work correctly
        pass
    
    @pytest.mark.navigation
    def test_sidebar_state_persists_across_pages(
        self, authenticated_page: Page
    ):
        """
        Test that sidebar collapse state persists across page navigation.
        
        TODO: Trainee should implement this test (advanced)
        """
        # GIVEN: User collapses sidebar on products page
        # WHEN: They navigate to inventory page
        # THEN: Sidebar should still be collapsed
        pass


class TestActiveNavHighlight:
    """Test suite for active navigation highlighting."""
    
    @pytest.mark.navigation
    def test_products_nav_highlighted_on_products_page(
        self, authenticated_page: Page
    ):
        """
        Test Products nav link is highlighted on products page.
        
        TODO: Trainee should implement this test
        """
        # GIVEN: User is on products page
        # THEN: Products nav link should have active styling
        pass
    
    @pytest.mark.navigation
    def test_inventory_nav_highlighted_on_inventory_page(
        self, authenticated_page: Page
    ):
        """
        Test Inventory nav link is highlighted on inventory page.
        
        TODO: Trainee should implement this test
        """
        pass
    
    @pytest.mark.navigation
    def test_orders_nav_highlighted_on_orders_page(
        self, authenticated_page: Page
    ):
        """
        Test Orders nav link is highlighted on orders page.
        
        TODO: Trainee should implement this test
        """
        pass


class TestUserInfoDisplay:
    """Test suite for user info display in sidebar."""
    
    @pytest.mark.navigation
    def test_user_name_displayed(self, authenticated_page: Page):
        """
        Test that user name is displayed in sidebar.
        
        TODO: Trainee should implement this test
        """
        # GIVEN: User is logged in
        # THEN: Their name should be displayed in the sidebar
        pass
    
    @pytest.mark.navigation
    def test_user_email_displayed(self, authenticated_page: Page):
        """
        Test that user email is displayed in sidebar.
        
        TODO: Trainee should implement this test
        """
        pass
    
    @pytest.mark.navigation
    def test_user_info_hidden_when_sidebar_collapsed(
        self, authenticated_page: Page
    ):
        """
        Test that user info is hidden when sidebar is collapsed.
        
        TODO: Trainee should implement this test
        """
        # GIVEN: Sidebar is collapsed
        # THEN: User name and email should not be visible
        # BUT: Logout button should still be visible as an icon
        pass
