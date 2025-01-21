from databases import Database
from sqlalchemy import create_engine, MetaData
from utils.config import config  # Import the config object
import logging

# Logger for this file
logger = logging.getLogger(__name__)

# Define the database URL from the configuration
DATABASE_URL = config.DATABASE_URL
logger.info(f"Database connection URL: {DATABASE_URL}")

# Create a Database object
database = Database(DATABASE_URL)

# Create SQLAlchemy engine and metadata for migrations
engine = create_engine(DATABASE_URL)
metadata = MetaData()