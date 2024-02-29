###################################################################################################
#######################################       IMPORTS       #######################################
###################################################################################################
import sys
import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Add the parent directory (Library-Management) to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.user import User, Base
from modules.book import Book
from modules.transaction import Transaction
from modules.config import load_admin_accounts
###################################################################################################
####################################       CONFIGURATION       ####################################
###################################################################################################
# Initialize the SQLAlchemy engine for sqlite
engine = create_engine('sqlite:///transactions_test.db')  # Adjust the database URL as needed

# Create the Base tables for each class
Base.metadata.create_all(engine)

# Create a Session class and bind the engine to it
Session = sessionmaker(bind=engine)

# Create session object
session = Session()

# Load books into the test database
load_transactions(session, "transactions_test.json")
###################################################################################################
################################       SETTER/GETTER TESTS       ##################################
###################################################################################################
def test_valid_user_id():
    ...
    
def test_invalid_user_id():
    ...

def test_valid_book_id():
    ...
    
def test_invalid_book_id():
    ...
    
def test_valid_type():
    ...
    
def test_invalid_type():
    ...
    
def test_valid_checkout_date():
    ...
    
def test_invalid_checkout_date():
    ...
    
def test_valid_return_date():
    ...
    
def test_invalid_return_date():
    ...
    
def test_valid_fee():
    ...
    
def test_invalid_fee():
    ...
    
def test_valid_status():
    ...
    
def test_invalid_status():
    ...
###################################################################################################
#################################       CLASSMETHOD TESTS       ###################################
###################################################################################################
def test_register():
    ...