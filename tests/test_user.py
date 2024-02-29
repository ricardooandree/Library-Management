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
from modules.transaction import Transaction
from modules.config import load_admin_accounts
###################################################################################################
####################################       CONFIGURATION       ####################################
###################################################################################################
# Initialize the SQLAlchemy engine for sqlite
engine = create_engine('sqlite:///test_user.db')  # Adjust the database URL as needed

# Create the Base tables for each class
Base.metadata.create_all(engine)

# Create a Session class and bind the engine to it
Session = sessionmaker(bind=engine)

# Create session object
session = Session()

# Load books into the test database
load_admin_accounts(session, "users_test.json")
###################################################################################################
################################       SETTER/GETTER TESTS       ##################################
###################################################################################################
def test_valid_username():
    # Test valid username
    user = User()
    user.set_username("valid_username") == True
    assert user.get_username() == "valid_username"

def test_invalid_username():
    # Test invalid username
    user = User()
    with pytest.raises(ValueError):
        user.set_username(1)   # Not string
    
    with pytest.raises(ValueError):
        user.set_username("")   # Empty string
        
    with pytest.raises(ValueError):
        user.set_username("Lorem ipsum dolor sit amet, consectetur adipiscing elit")   # String bigger than 50 characters
    
    with pytest.raises(ValueError):
        user.set_username(" username ")   # Leading and trailing spaces
        
    with pytest.raises(ValueError):
        user.set_username("user,name")   # Special characters 

def test_valid_password():
    # Test valid password
    user = User()
    assert user.set_password("valid_password") == None

def test_invalid_password():
    # Test invalid password
    user = User()
    with pytest.raises(ValueError):
        user.set_password(1)   # Not string
    
    with pytest.raises(ValueError):
        user.set_password("")   # Empty string
        
    with pytest.raises(ValueError):
        user.set_password("Lorem ipsum dolor sit amet, consectetur adipiscing elit")   # String bigger than 50 characters
    
    with pytest.raises(ValueError):
        user.set_password(" password ")   # Leading and trailing spaces
        
    with pytest.raises(ValueError):
        user.set_password("pass word")   # String containing spaces

def test_valid_is_admin():
    # Test valid is_admin
    user = User()
    assert user.set_is_admin(True) == None

def test_invalid_is_admin():
    # Test invalid is_admin
    user = User()
    with pytest.raises(ValueError):
        user.set_is_admin(1) # Integer - Not boolean
        
    with pytest.raises(ValueError):
        user.set_is_admin("") # Empty string - Not boolean
    
    with pytest.raises(ValueError):
        user.set_is_admin("ricardo") # String - Not boolean

def test_valid_total_fee():
    # Test valid total fee
    user = User()
    user.set_total_fee(100.50)
    assert user.get_total_fee() == 100.50
    
def test_invalid_total_fee():
    # Test invalid total fee
    user = User()
    with pytest.raises(ValueError):
        user.set_total_fee(1)   # Integer - Not float
    
    with pytest.raises(ValueError):
        user.set_total_fee("")   # Empty string - Not float
        
    with pytest.raises(ValueError):
        user.set_total_fee("Lorem ipsum dolor sit amet")   # String - Not float
    
    with pytest.raises(ValueError):
        user.set_total_fee(-1.50)   # Negative float

###################################################################################################
#################################       CLASSMETHOD TESTS       ###################################
###################################################################################################
def test_validate():
    # Test validate method
    assert User.validate(session, "ricardo", "password1", "password1") == False
    
    assert User.validate(session, "ricardo", "password1", "password2") == False
    
    assert User.validate(session, "john", "password1", "password1") == True

def test_authenticate():
    # Test authenticate method
    assert User.authenticate(session, "ricardo", "password1") != None
    
    assert User.authenticate(session, "ricardo", "password2") == None

def test_register():
    # Test register method
    assert User.register(session, "new_user", "iloveyou") != False

def test_rent_book():
    # Test rent_book method
    user = User()
    user.set_total_fee(0.00)
    assert user.rent_book(session, 10.00) == True

    assert user.get_total_fee() == 10.00

def test_return_book():
    # Test return_book method
    user = User()
    user.set_total_fee(20.00)
    assert user.return_book(session, 10.00) == True
    
    assert user.get_total_fee() == 10.00
    
    
# TODO:
# TODO:
# TODO:

# def test_authenticate_id():