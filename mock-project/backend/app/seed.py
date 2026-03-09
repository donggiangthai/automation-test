"""
Seed database with sample data
"""
from app.database import SessionLocal
from app.models import Product, Inventory, Order, User
from app.config import settings


def seed_database():
    """Populate database with sample data"""
    db = SessionLocal()
    
    try:
        # Check if data exists
        if db.query(Product).first():
            print("Database already seeded")
            return
        
        # Create test user
        test_user = User(
            email=settings.TEST_USER_EMAIL,
            name="Test User"
        )
        db.add(test_user)
        
        # Create products
        products_data = [
            {"name": "Laptop Pro 15", "description": "High-performance laptop with 16GB RAM", "price": 1299.99, "category": "Electronics"},
            {"name": "Wireless Mouse", "description": "Ergonomic wireless mouse", "price": 49.99, "category": "Electronics"},
            {"name": "Mechanical Keyboard", "description": "RGB mechanical keyboard", "price": 129.99, "category": "Electronics"},
            {"name": "USB-C Hub", "description": "7-in-1 USB-C hub", "price": 59.99, "category": "Electronics"},
            {"name": "Monitor 27\"", "description": "4K IPS monitor", "price": 449.99, "category": "Electronics"},
            {"name": "Webcam HD", "description": "1080p webcam with microphone", "price": 79.99, "category": "Electronics"},
            {"name": "Headphones Pro", "description": "Noise-cancelling wireless headphones", "price": 249.99, "category": "Electronics"},
            {"name": "Desk Lamp", "description": "LED desk lamp with adjustable brightness", "price": 34.99, "category": "Office"},
            {"name": "Office Chair", "description": "Ergonomic office chair", "price": 299.99, "category": "Furniture"},
            {"name": "Standing Desk", "description": "Electric standing desk", "price": 599.99, "category": "Furniture"},
        ]
        
        products = []
        for data in products_data:
            product = Product(**data)
            db.add(product)
            products.append(product)
        
        db.flush()  # Get IDs
        
        # Create inventory for each product
        inventory_data = [
            {"product_id": 1, "quantity": 50, "min_quantity": 10, "location": "Warehouse A"},
            {"product_id": 2, "quantity": 200, "min_quantity": 50, "location": "Warehouse A"},
            {"product_id": 3, "quantity": 75, "min_quantity": 20, "location": "Warehouse A"},
            {"product_id": 4, "quantity": 150, "min_quantity": 30, "location": "Warehouse B"},
            {"product_id": 5, "quantity": 25, "min_quantity": 5, "location": "Warehouse B"},
            {"product_id": 6, "quantity": 100, "min_quantity": 25, "location": "Warehouse A"},
            {"product_id": 7, "quantity": 60, "min_quantity": 15, "location": "Warehouse B"},
            {"product_id": 8, "quantity": 300, "min_quantity": 50, "location": "Warehouse C"},
            {"product_id": 9, "quantity": 40, "min_quantity": 10, "location": "Warehouse C"},
            {"product_id": 10, "quantity": 15, "min_quantity": 5, "location": "Warehouse C"},
        ]
        
        for data in inventory_data:
            inventory = Inventory(**data)
            db.add(inventory)
        
        # Create sample orders
        orders_data = [
            {"customer_name": "John Smith", "customer_email": "john@example.com", "product_id": 1, "quantity": 2, "total_amount": 2599.98, "status": "delivered", "notes": "Express shipping"},
            {"customer_name": "Jane Doe", "customer_email": "jane@example.com", "product_id": 2, "quantity": 5, "total_amount": 249.95, "status": "shipped", "notes": None},
            {"customer_name": "Bob Wilson", "customer_email": "bob@example.com", "product_id": 3, "quantity": 1, "total_amount": 129.99, "status": "processing", "notes": "Gift wrap requested"},
            {"customer_name": "Alice Brown", "customer_email": "alice@example.com", "product_id": 5, "quantity": 1, "total_amount": 449.99, "status": "pending", "notes": None},
            {"customer_name": "Charlie Davis", "customer_email": "charlie@example.com", "product_id": 7, "quantity": 2, "total_amount": 499.98, "status": "pending", "notes": "Corporate order"},
            {"customer_name": "Eva Martinez", "customer_email": "eva@example.com", "product_id": 4, "quantity": 3, "total_amount": 179.97, "status": "shipped", "notes": None},
            {"customer_name": "Frank Lee", "customer_email": "frank@example.com", "product_id": 9, "quantity": 1, "total_amount": 299.99, "status": "delivered", "notes": "Assembly required"},
            {"customer_name": "Grace Kim", "customer_email": "grace@example.com", "product_id": 10, "quantity": 1, "total_amount": 599.99, "status": "processing", "notes": "White color"},
        ]
        
        for data in orders_data:
            order = Order(**data)
            db.add(order)
        
        db.commit()
        print("Database seeded successfully!")
        
    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
