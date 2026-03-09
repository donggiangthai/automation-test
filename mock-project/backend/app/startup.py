"""
Application startup script.

Handles database connection, table creation, and seeding.
This script is called by Docker container on startup.
"""

import sys
import time
import logging

import psycopg2
from psycopg2 import OperationalError

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)


def wait_for_database(database_url: str, max_retries: int = 30, retry_interval: int = 2) -> bool:
    """
    Wait for database to be ready.
    
    Args:
        database_url: PostgreSQL connection string
        max_retries: Maximum number of retries
        retry_interval: Seconds between retries
    
    Returns:
        True if database is ready, False otherwise
    """
    logger.info("🔄 Waiting for database connection...")
    
    for attempt in range(1, max_retries + 1):
        try:
            conn = psycopg2.connect(database_url)
            conn.close()
            logger.info("✅ Database connection established!")
            return True
        except OperationalError as e:
            logger.warning(f"⏳ Attempt {attempt}/{max_retries}: Database not ready - {e}")
            time.sleep(retry_interval)
    
    logger.error("❌ Could not connect to database after maximum retries")
    return False


def create_tables() -> None:
    """Create all database tables."""
    logger.info("📦 Creating database tables...")
    
    from app.database import engine, Base
    from app import models  # noqa: F401 - import to register models
    
    Base.metadata.create_all(bind=engine)
    logger.info("✅ Database tables created!")


def seed_database() -> None:
    """Seed database with initial data."""
    logger.info("🌱 Seeding database with sample data...")
    
    from app.seed import seed_database as run_seed
    run_seed()
    
    logger.info("✅ Database seeding complete!")


def startup() -> bool:
    """
    Run all startup tasks.
    
    Returns:
        True if all tasks completed successfully
    """
    from app.config import settings
    
    logger.info("=" * 50)
    logger.info("🚀 Starting application initialization...")
    logger.info("=" * 50)
    
    # Step 1: Wait for database
    if not wait_for_database(settings.DATABASE_URL):
        return False
    
    # Step 2: Create tables
    try:
        create_tables()
    except Exception as e:
        logger.error(f"❌ Failed to create tables: {e}")
        return False
    
    # Step 3: Seed database
    try:
        seed_database()
    except Exception as e:
        logger.error(f"❌ Failed to seed database: {e}")
        return False
    
    logger.info("=" * 50)
    logger.info("✅ Application initialization complete!")
    logger.info("=" * 50)
    
    return True


if __name__ == "__main__":
    success = startup()
    sys.exit(0 if success else 1)
