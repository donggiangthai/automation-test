"""
Shared fixtures for E2E tests.

This file contains fixtures used across all test files.
Trainees should study this file to understand:
1. How to create reusable fixtures
2. Page Object Pattern integration
3. Test isolation and cleanup
4. Environment configuration
"""

import os
import pytest
from playwright.sync_api import Page, Browser, BrowserContext
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")
API_URL = os.getenv("API_URL", "http://localhost:8000")


# ==============================================================================
# Browser & Context Fixtures
# ==============================================================================

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Configure browser context for all tests.
    
    This fixture runs once per test session and configures:
    - Viewport size
    - Base URL
    - Storage state (for auth persistence)
    """
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "base_url": BASE_URL,
    }


# ==============================================================================
# Authentication Fixtures
# ==============================================================================

@pytest.fixture
def authenticated_page(page: Page) -> Page:
    """
    Provide an authenticated page for tests that require login.
    
    Uses dev login to bypass Google SSO for testing.
    
    Usage:
        def test_something(authenticated_page):
            authenticated_page.goto("/products")
    """
    # Navigate to login page
    page.goto("/login")
    
    # Use dev login (bypass auth mode)
    page.click('[data-testid="dev-login-button"]')
    
    # Wait for redirect to products page
    page.wait_for_url("**/products")
    
    return page


@pytest.fixture
def guest_page(page: Page) -> Page:
    """
    Provide a non-authenticated page.
    
    Clears any existing auth state.
    
    Usage:
        def test_login_redirect(guest_page):
            guest_page.goto("/products")
            expect(guest_page).to_have_url("/login")
    """
    # Clear local storage
    page.evaluate("localStorage.clear()")
    return page


# ==============================================================================
# Page Object Fixtures
# ==============================================================================

# TODO: Trainee should implement these fixtures after creating Page Objects
#
# @pytest.fixture
# def login_page(page: Page) -> LoginPage:
#     """Provide LoginPage object."""
#     return LoginPage(page)
#
# @pytest.fixture
# def products_page(authenticated_page: Page) -> ProductsPage:
#     """Provide authenticated ProductsPage object."""
#     return ProductsPage(authenticated_page)
#
# @pytest.fixture
# def inventory_page(authenticated_page: Page) -> InventoryPage:
#     """Provide authenticated InventoryPage object."""
#     return InventoryPage(authenticated_page)
#
# @pytest.fixture
# def orders_page(authenticated_page: Page) -> OrdersPage:
#     """Provide authenticated OrdersPage object."""
#     return OrdersPage(authenticated_page)


# ==============================================================================
# Helper Fixtures
# ==============================================================================

@pytest.fixture
def base_url() -> str:
    """Provide base URL for tests."""
    return BASE_URL


@pytest.fixture
def api_url() -> str:
    """Provide API URL for tests."""
    return API_URL


# ==============================================================================
# Cleanup Fixtures
# ==============================================================================

@pytest.fixture(autouse=True)
def cleanup_after_test(page: Page):
    """
    Automatic cleanup after each test.
    
    This fixture runs after every test to ensure test isolation.
    """
    yield
    
    # Clear any pending changes in the UI
    # This prevents state leakage between tests
    try:
        reset_button = page.locator('[data-testid="reset-button"]')
        if reset_button.is_visible() and reset_button.is_enabled():
            reset_button.click()
    except:
        pass  # Ignore if not on a page with reset button
