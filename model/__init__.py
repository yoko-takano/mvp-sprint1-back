from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# Importing elements defined in model
from model.base import Base
from model.asset_administration_shell import AssetAdministrationShell


db_path = "database/"

# Verifies if the directory does not exist
if not os.path.exists(db_path):

    # If it doesn't exist, creates the directory
    os.makedirs(db_path)

# Database URL for local SQLite access
db_url = 'sqlite:///%s/db.sqlite3' % db_path

# Creates the connection engine to the database
engine = create_engine(db_url, echo=False)

# Session maker instance bound to the engine
Session = sessionmaker(bind=engine)

# Creates the database if it doesn't exist
if not database_exists(engine.url):
    create_database(engine.url)

# Creates the tables in the database if they do not exist
Base.metadata.create_all(engine)
