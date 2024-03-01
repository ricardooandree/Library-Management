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
from modules.config import load_transactions
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
    # Test valid user id input
    transaction = Transaction()
    transaction.set_user_id(5)
    assert transaction.get_user_id() == 5
    
def test_invalid_user_id():
    # Test invalid user id input
    transaction = Transaction()

    with pytest.raises(ValueError):
        transaction.set_user_id("")   # Empty string
        
    with pytest.raises(ValueError):
        transaction.set_user_id("foo")   # String
        
    with pytest.raises(ValueError):
        transaction.set_user_id(9.99)   # Float
        
    with pytest.raises(ValueError):
        transaction.set_user_id(-1)   # Negative integer
    
    with pytest.raises(ValueError):
        transaction.set_user_id(0)   # Zero integer

def test_valid_book_id():
    # Test valid book id input
    transaction = Transaction()
    transaction.set_book_id(5)
    assert transaction.get_book_id() == 5
    
def test_invalid_book_id():
    # Test invalid book id input
    transaction = Transaction()

    with pytest.raises(ValueError):
        transaction.set_book_id("")   # Empty string
        
    with pytest.raises(ValueError):
        transaction.set_book_id("foo")   # String
        
    with pytest.raises(ValueError):
        transaction.set_book_id(9.99)   # Float
        
    with pytest.raises(ValueError):
        transaction.set_book_id(-1)   # Negative integer
    
    with pytest.raises(ValueError):
        transaction.set_book_id(0)   # Zero integer
    
def test_valid_type():
    # Test valid type input
    transaction = Transaction()
    transaction.set_type("Rental")
    assert transaction.get_type() == "Rental"
    
def test_invalid_type():
    # Test invalid type input
    transaction = Transaction()
    
    with pytest.raises(ValueError):
        transaction.set_type(1)   # Integer
        
    with pytest.raises(ValueError):
        transaction.set_type(9.99)   # Float
    
    with pytest.raises(ValueError):
        transaction.set_type("")   # Empty string
        
    with pytest.raises(ValueError):
        transaction.set_type("foo")   # Wrong string
    
def test_valid_checkout_date():
    # Test valid checkout date input
    checkout_date = datetime(2024, 3, 1).date()
    
    transaction = Transaction()
    transaction.set_checkout_date(checkout_date)
    
    # Check if the retrieved checkout date matches the one set
    assert transaction.get_checkout_date() == checkout_date
    
def test_invalid_checkout_date():
    # Test invalid checkout date input
    transaction = Transaction()
    
    with pytest.raises(ValueError):
        transaction.set_checkout_date("")   # Empty string
        
    with pytest.raises(ValueError):
        transaction.set_checkout_date("foo")   # String
    
    with pytest.raises(ValueError):
        transaction.set_checkout_date("01-03-2024")   # String
         
    with pytest.raises(ValueError):
        transaction.set_checkout_date(9.99)   # Float
        
    with pytest.raises(ValueError):
        transaction.set_checkout_date(-1)   # Negative integer
    
    with pytest.raises(ValueError):
        transaction.set_checkout_date(0)   # Zero integer
    
def test_valid_return_date():
    # Test valid return date input
    return_date = datetime(2024, 3, 10).date()
    
    transaction = Transaction()
    transaction.set_return_date(return_date)
    
    # Check if the retrieved return date matches the one set
    assert transaction.get_return_date() == return_date
    
def test_invalid_return_date():
    # Test invalid return date input
    transaction = Transaction()
    
    with pytest.raises(ValueError):
        transaction.set_return_date("")   # Empty string
        
    with pytest.raises(ValueError):
        transaction.set_return_date("foo")   # String
    
    with pytest.raises(ValueError):
        transaction.set_return_date("01-03-2024")   # String
         
    with pytest.raises(ValueError):
        transaction.set_return_date(9.99)   # Float
        
    with pytest.raises(ValueError):
        transaction.set_return_date(-1)   # Negative integer
    
    with pytest.raises(ValueError):
        transaction.set_return_date(0)   # Zero integer
    
def test_valid_fee():
    # Test valid fee input
    transaction = Transaction()
    transaction.set_fee(9.99)
    assert transaction.get_fee() == 9.99
    
def test_invalid_fee():
    # Test invalid fee input
    transaction = Transaction()
    
    with pytest.raises(ValueError):
        transaction.set_fee("")   # Empty string
        
    with pytest.raises(ValueError):
        transaction.set_fee("foo")   # String
        
    with pytest.raises(ValueError):
        transaction.set_fee(-1)   # Negative integer
    
    with pytest.raises(ValueError):
        transaction.set_fee(0)   # Zero integer
        
    with pytest.raises(ValueError):
        transaction.set_fee(1)   # Integer
        
    with pytest.raises(ValueError):
        transaction.set_fee(-1.99)   # Negative float
    
def test_valid_status():
    # Test valid status input
    transaction = Transaction()
    transaction.set_status(True)
    assert transaction.get_status() == True
    
def test_invalid_status():
    # Test invalid status input
    transaction = Transaction()
    
    with pytest.raises(ValueError):
        transaction.set_status("")   # Empty string
        
    with pytest.raises(ValueError):
        transaction.set_status("foo")   # String
        
    with pytest.raises(ValueError):
        transaction.set_status(9.99)   # Float
    
    with pytest.raises(ValueError):
        transaction.set_status(1)   # Integer
    
###################################################################################################
#################################       CLASSMETHOD TESTS       ###################################
###################################################################################################
def test_authenticate_user_book():
    # Test authenticating a transaction by user and book
    assert Transaction.authenticate_user_book(session, 1, 1, type="Rental") is not None
    
    assert Transaction.authenticate_user_book(session, 3, 1) is None

    assert Transaction.authenticate_user_book(session, 1, 5) is None
    
def test_authenticate_book_id():
    # Test authenticating a transaction by book id
    assert Transaction.authenticate_book_id(session, 1, type="Rental") is not None
    
    assert Transaction.authenticate_book_id(session, 5) is None

def test_authenticate_user_id():
    # Test authenticating a transaction by user id
    assert Transaction.authenticate_user_id(session, 1, type="Rental") is not None
    
    assert Transaction.authenticate_user_id(session, 5) is None
    
def test_register():
    # Test registering a transaction
    checkout_date = datetime.strptime("2024-03-01", '%Y-%m-%d').date()
    return_date = datetime.strptime("2024-04-12", '%Y-%m-%d').date()
        
    assert Transaction.register(session, 1, 1, checkout_date, return_date, 12.99, True, "Return") == True
    
def test_get_all_username():
    # Test get all transactions by user username

    user = User.register(session, "new-user", "123")
    
    # Register transaction in that username
    checkout_date = datetime.strptime("2024-03-05", '%Y-%m-%d').date()
    return_date = datetime.strptime("2024-04-05", '%Y-%m-%d').date()
    
    Transaction.register(session, user.get_id(), 1, checkout_date, return_date, 12.99, True, "Return")
                         
    assert Transaction.get_all_username(session, user.get_id()) is not None
    
def test_get_all_isbn():
    # Test get all transactions by ISBN
    
    book = Book.register(session, "OOP Python Fundamentals", "Ricardo Silva", "HaperCollins", "Educational", 1, "25-02-2024", "Discover", 9.99, "111-2-33-444444-5")
    
    # Register transaction for that ISBN
    checkout_date = datetime.strptime("2024-03-05", '%Y-%m-%d').date()
    return_date = datetime.strptime("2024-04-05", '%Y-%m-%d').date()
    
    Transaction.register(session, 1, book.get_id(), checkout_date, return_date, 12.99, True, "Return")
    
    assert Transaction.get_all_isbn(session, book.get_id()) is not None
    
def test_get_all_type():
    # Test get all transactions by type
    transactions = Transaction.get_all_type(session, "Rental")
    assert len(transactions) == 2
    
    transactions = Transaction.get_all_type(session, "Return")
    assert len(transactions) == 4