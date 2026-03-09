"""
Login Page Object.

Represents the login page and provides methods for authentication.
"""

from playwright.sync_api import Page, Locator, expect
from .base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object for the Login page.
    
    Provides methods to:
    - Login with Google SSO
    - Login with dev bypass
    - Check login page state
    
    Trainees: Notice how we encapsulate all login-related
    interactions in this class.
    """
    
    PATH = "/login"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    # ==========================================================================
    # Navigation
    # ==========================================================================
    
    def navigate(self) -> "LoginPage":
        """Navigate to login page."""
        self.goto(self.PATH)
        return self
    
    # ==========================================================================
    # Locators
    # ==========================================================================
    
    @property
    def google_login_button(self) -> Locator:
        """Get Google SSO login button."""
        return self.page.locator('[data-testid="google-login-button"]')
    
    @property
    def dev_login_button(self) -> Locator:
        """Get Dev login bypass button."""
        return self.page.locator('[data-testid="dev-login-button"]')
    
    @property
    def page_title(self) -> Locator:
        """Get page title element."""
        return self.page.locator("h1")
    
    @property
    def login_container(self) -> Locator:
        """Get main login container."""
        return self.page.locator('[data-testid="login-container"]')
    
    # ==========================================================================
    # Actions
    # ==========================================================================
    
    def login_with_google(self) -> None:
        """
        Click Google SSO login button.
        
        Note: This will redirect to Google OAuth flow.
        For E2E tests, prefer using dev_login() instead.
        """
        self.google_login_button.click()
    
    def login_with_dev_bypass(self) -> None:
        """
        Login using dev bypass mode.
        
        This skips Google OAuth and logs in as a test user.
        Useful for E2E testing without external dependencies.
        """
        self.dev_login_button.click()
        self.page.wait_for_url("**/products")
    
    # ==========================================================================
    # Assertions
    # ==========================================================================
    
    def is_loaded(self) -> bool:
        """
        Check if login page is fully loaded.
        
        Returns:
            True if page is loaded and ready
        """
        try:
            self.google_login_button.wait_for(state="visible", timeout=5000)
            return True
        except:
            return False
    
    def assert_on_login_page(self) -> None:
        """Assert we are on the login page."""
        expect(self.page).to_have_url("**/login")
        expect(self.google_login_button).to_be_visible()
    
    def assert_google_button_visible(self) -> None:
        """Assert Google login button is visible."""
        expect(self.google_login_button).to_be_visible()
    
    def assert_dev_button_visible(self) -> None:
        """Assert dev login button is visible (only in dev mode)."""
        expect(self.dev_login_button).to_be_visible()
