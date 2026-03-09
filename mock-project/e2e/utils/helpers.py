"""
Helper utilities for E2E tests.

Contains utility functions that can be used across multiple tests.
"""

import random
import string
from datetime import datetime
from playwright.sync_api import Page, Response


def wait_for_api_response(
    page: Page,
    url_pattern: str,
    method: str = "GET",
    timeout: int = 10000
) -> Response:
    """
    Wait for an API response matching the given pattern.
    
    Useful for waiting for data to load before asserting.
    
    Args:
        page: Playwright Page instance
        url_pattern: URL pattern to match (e.g., "**/api/products")
        method: HTTP method to match
        timeout: Timeout in milliseconds
    
    Returns:
        The matched Response object
    
    Example:
        response = wait_for_api_response(page, "**/api/products")
        assert response.status == 200
    """
    with page.expect_response(
        lambda r: url_pattern in r.url and r.request.method == method,
        timeout=timeout
    ) as response_info:
        pass
    return response_info.value


def generate_test_data(data_type: str, **kwargs) -> dict:
    """
    Generate test data for various entities.
    
    Args:
        data_type: Type of data to generate ("product", "inventory", "order")
        **kwargs: Override specific fields
    
    Returns:
        Dictionary with generated test data
    
    Example:
        product = generate_test_data("product", name="Custom Name")
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_suffix = "".join(random.choices(string.ascii_lowercase, k=4))
    
    generators = {
        "product": lambda: {
            "name": f"Test Product {timestamp}_{random_suffix}",
            "sku": f"SKU-{timestamp}",
            "price": round(random.uniform(10.0, 1000.0), 2),
            "category": random.choice(["Electronics", "Clothing", "Books"]),
            "description": f"Test description for product {random_suffix}",
        },
        "inventory": lambda: {
            "quantity": random.randint(0, 500),
            "location": f"Warehouse-{random.choice(['A', 'B', 'C'])}-{random.randint(1, 99)}",
            "min_quantity": 10,
            "max_quantity": 500,
        },
        "order": lambda: {
            "customer_name": f"Test Customer {random_suffix}",
            "customer_email": f"test.{random_suffix}@example.com",
            "status": random.choice(["pending", "processing", "shipped"]),
            "total_amount": round(random.uniform(50.0, 5000.0), 2),
            "shipping_address": f"{random.randint(1, 999)} Test Street, City {random_suffix}",
        },
    }
    
    if data_type not in generators:
        raise ValueError(f"Unknown data type: {data_type}")
    
    data = generators[data_type]()
    data.update(kwargs)  # Override with provided kwargs
    return data


def get_platform_modifier_key() -> str:
    """
    Get the platform-specific modifier key for multi-select.
    
    Returns:
        "Meta" for Mac, "Control" for Windows/Linux
    """
    # In tests, we typically use "Control" which works cross-platform
    # For Mac-specific behavior, use "Meta"
    return "Control"


def format_currency(amount: float) -> str:
    """
    Format a number as currency string.
    
    Args:
        amount: The amount to format
    
    Returns:
        Formatted string (e.g., "1,234.56")
    """
    return f"{amount:,.2f}"


def parse_count_from_text(text: str) -> int:
    """
    Extract count number from text like "5 cell(s) selected".
    
    Args:
        text: Text containing a count
    
    Returns:
        The extracted count
    
    Example:
        count = parse_count_from_text("5 cell(s) selected")  # Returns 5
    """
    import re
    match = re.search(r"(\d+)", text)
    return int(match.group(1)) if match else 0
