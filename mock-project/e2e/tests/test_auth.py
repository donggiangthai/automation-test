"""
Authentication Tests.

These tests verify login and logout functionality.

Trainees: This file contains some complete tests as examples,
and some TODO tests for you to implement.
"""

import pytest
from playwright.sync_api import Page, expect
from pages import LoginPage


class TestAuthentication:
    """Test suite for authentication functionality."""
    
    @pytest.mark.auth
    @pytest.mark.smoke
    def test_login_page_loads(self, page: Page):
        """
        Test that login page loads correctly.
        
        GIVEN: A user navigates to the application
        WHEN: They are not authenticated
        THEN: They should see the login page with Google SSO button
        """
        login_page = LoginPage(page)
        login_page.navigate()
        
        login_page.assert_on_login_page()
        login_page.assert_google_button_visible()
    
    @pytest.mark.auth
    @pytest.mark.smoke
    def test_dev_login_bypass(self, page: Page):
        """
        Test dev login bypass works correctly.
        
        GIVEN: A user is on the login page
        WHEN: They click the dev login button
        THEN: They should be redirected to the products page
        """
        login_page = LoginPage(page)
        login_page.navigate()
        
        login_page.login_with_dev_bypass()
        
        expect(page).to_have_url("**/products")
    
    @pytest.mark.auth
    def test_unauthenticated_redirect(self, guest_page: Page):
        """
        Test that unauthenticated users are redirected to login.
        
        GIVEN: A user is not authenticated
        WHEN: They try to access a protected page
        THEN: They should be redirected to the login page
        """
        # TODO: Trainee should implement this test
        # Hint:
        # 1. Navigate directly to /products
        # 2. Assert that the page redirects to /login
        pass
    
    @pytest.mark.auth
    def test_logout_functionality(self, authenticated_page: Page):
        """
        Test that logout works correctly.
        
        GIVEN: A user is logged in
        WHEN: They click the logout button
        THEN: They should be redirected to the login page
        AND: They should not be able to access protected pages
        """
        # TODO: Trainee should implement this test
        # Hint:
        # 1. Use BasePage or create page object from authenticated_page
        # 2. Click the logout button
        # 3. Assert redirect to login page
        # 4. Try to navigate to /products
        # 5. Assert still on login page
        pass
    
    @pytest.mark.auth
    def test_session_persistence(self, page: Page):
        """
        Test that user session persists across page reloads.
        
        GIVEN: A user has logged in
        WHEN: They reload the page
        THEN: They should still be authenticated
        """
        # TODO: Trainee should implement this test
        # Hint:
        # 1. Login using dev bypass
        # 2. Reload the page (page.reload())
        # 3. Assert still on products page or can navigate to it
        pass


class TestLoginPageUI:
    """Test suite for login page UI elements."""
    
    @pytest.mark.auth
    def test_login_page_has_google_button(self, page: Page):
        """Test Google login button is visible."""
        login_page = LoginPage(page)
        login_page.navigate()
        
        login_page.assert_google_button_visible()
    
    @pytest.mark.auth
    def test_login_page_has_dev_button_in_dev_mode(self, page: Page):
        """
        Test dev login button is visible in development mode.
        
        Note: This button should only appear when BYPASS_AUTH is enabled.
        """
        login_page = LoginPage(page)
        login_page.navigate()
        
        # In dev mode, dev login button should be visible
        login_page.assert_dev_button_visible()
    
    @pytest.mark.auth
    def test_login_page_title(self, page: Page):
        """
        Test login page has correct title.
        
        TODO: Trainee should implement this test
        """
        # Hint:
        # 1. Navigate to login page
        # 2. Assert page title or h1 contains expected text
        pass
