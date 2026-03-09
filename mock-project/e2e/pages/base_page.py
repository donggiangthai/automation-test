"""
Base Page Object class.

All page objects should inherit from this class.
It provides common functionality like:
- Page navigation
- Element waiting
- Screenshot capture
- Sidebar interaction
"""

from playwright.sync_api import Page, Locator, expect


class BasePage:
    """
    Base class for all Page Objects.
    
    Provides shared functionality for all pages including:
    - Navigation helpers
    - Sidebar controls
    - Common element accessors
    - Wait utilities
    
    Trainees: Study this class to understand the Page Object pattern.
    """
    
    def __init__(self, page: Page):
        """
        Initialize the base page.
        
        Args:
            page: Playwright Page instance
        """
        self.page = page
    
    # ==========================================================================
    # Navigation
    # ==========================================================================
    
    def goto(self, path: str = "") -> None:
        """
        Navigate to a path relative to base URL.
        
        Args:
            path: Path to navigate to (e.g., "/products")
        """
        self.page.goto(path)
    
    def wait_for_page_load(self) -> None:
        """Wait for page to finish loading."""
        self.page.wait_for_load_state("networkidle")
    
    def get_current_url(self) -> str:
        """Get current page URL."""
        return self.page.url
    
    # ==========================================================================
    # Sidebar
    # ==========================================================================
    
    @property
    def sidebar(self) -> Locator:
        """Get sidebar element."""
        return self.page.locator('[data-testid="sidebar"]')
    
    @property
    def sidebar_toggle(self) -> Locator:
        """Get sidebar toggle button."""
        return self.page.locator('[data-testid="sidebar-toggle"]')
    
    def toggle_sidebar(self) -> None:
        """Toggle sidebar expanded/collapsed state."""
        self.sidebar_toggle.click()
    
    def is_sidebar_collapsed(self) -> bool:
        """Check if sidebar is collapsed."""
        return self.sidebar.evaluate(
            'el => el.classList.contains("collapsed")'
        )
    
    def collapse_sidebar(self) -> None:
        """Collapse sidebar if expanded."""
        if not self.is_sidebar_collapsed():
            self.toggle_sidebar()
    
    def expand_sidebar(self) -> None:
        """Expand sidebar if collapsed."""
        if self.is_sidebar_collapsed():
            self.toggle_sidebar()
    
    # ==========================================================================
    # Navigation Links
    # ==========================================================================
    
    @property
    def nav_products(self) -> Locator:
        """Get Products navigation link."""
        return self.page.locator('[data-testid="nav-products"]')
    
    @property
    def nav_inventory(self) -> Locator:
        """Get Inventory navigation link."""
        return self.page.locator('[data-testid="nav-inventory"]')
    
    @property
    def nav_orders(self) -> Locator:
        """Get Orders navigation link."""
        return self.page.locator('[data-testid="nav-orders"]')
    
    def go_to_products(self) -> None:
        """Navigate to Products page via sidebar."""
        self.nav_products.click()
        self.page.wait_for_url("**/products")
    
    def go_to_inventory(self) -> None:
        """Navigate to Inventory page via sidebar."""
        self.nav_inventory.click()
        self.page.wait_for_url("**/inventory")
    
    def go_to_orders(self) -> None:
        """Navigate to Orders page via sidebar."""
        self.nav_orders.click()
        self.page.wait_for_url("**/orders")
    
    # ==========================================================================
    # User Info
    # ==========================================================================
    
    @property
    def user_name(self) -> Locator:
        """Get user name element."""
        return self.page.locator('[data-testid="user-name"]')
    
    @property
    def user_email(self) -> Locator:
        """Get user email element."""
        return self.page.locator('[data-testid="user-email"]')
    
    @property
    def logout_button(self) -> Locator:
        """Get logout button."""
        return self.page.locator('[data-testid="logout-button"]')
    
    def logout(self) -> None:
        """Click logout button."""
        self.logout_button.click()
        self.page.wait_for_url("**/login")
    
    def get_logged_in_user(self) -> dict:
        """
        Get currently logged in user info.
        
        Returns:
            dict with 'name' and 'email' keys
        """
        self.expand_sidebar()  # Ensure sidebar is expanded to see user info
        return {
            "name": self.user_name.text_content(),
            "email": self.user_email.text_content(),
        }
    
    # ==========================================================================
    # Screenshots
    # ==========================================================================
    
    def take_screenshot(self, name: str) -> None:
        """
        Take a screenshot for debugging.
        
        Args:
            name: Screenshot filename (without extension)
        """
        self.page.screenshot(path=f"screenshots/{name}.png")
    
    # ==========================================================================
    # Assertions (helpers)
    # ==========================================================================
    
    def assert_url_contains(self, path: str) -> None:
        """Assert current URL contains the given path."""
        expect(self.page).to_have_url(f"**{path}**")
    
    def assert_title_contains(self, text: str) -> None:
        """Assert page title contains the given text."""
        expect(self.page).to_have_title(f"*{text}*")
