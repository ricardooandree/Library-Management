###################################################################################################
#######################################       IMPORTS       #######################################
###################################################################################################
import os
import sys
import random 

from modules.menu import Menu
from modules.user import User, Base
from modules.book import Book
from modules.transaction import Transaction
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
###################################################################################################
#################################       APP CONFIGURATION        ##################################
###################################################################################################
# Initialize the SQLAlchemy engine for sqlite
engine = create_engine('sqlite:///library.db')  # Adjust the database URL as needed

# Create the Base tables for each class
Base.metadata.create_all(engine)
# FIXME: Base.metadata.create_all(engine, checkfirst=True)

# Create a Session class and bind the engine to it
Session = sessionmaker(bind=engine)

# Create session object
session = Session()
###################################################################################################
#####################################       FUNCTIONS        ######################################
###################################################################################################
def get_username():
    """Get username input from the user"""
    
    # Get user username
    while True:
        username = input("Enter username: ").strip()
        if username:
            return username
        else:
            print("Please enter username\n")
            
            
def get_password():
    """Get password input from the user"""
    
    # Get user password
    while True:
        password = input("Enter password: ").strip()
        if password:
            return password
        else:
            print("Please enter password\n")
            

def get_password_confirm():
    """Get password confirmation input from the user"""
    
    # Get user password confirmation
    while True:
        password_confirm = input("Enter password confirmation: ").strip()
        if password_confirm:
            return password_confirm
        else:
            print("Please enter password confirmation\n")
            
            
def register_form():
    """Register form, gets user input, validates it and handles validation cases"""
    
    # Get user input
    username = get_username()
    password = get_password()
    password_confirm = get_password_confirm()
    
    # Validate credentials
    if User.validate(session, username, password, password_confirm):
        # Register user
        User.register(session, username, password)
    else:
        # TODO: Implemente logic to handle wrong credentials
        #       Try again or Back to main menu ???
        ...
    

def register_user():
    """Register user"""
    
    # TODO: User register form with username and password before accessing the menu
    register_form()


def log_in_form():
    """Log in form, gets user input, validates it and handles validation cases"""
    
    # Get user input
    username = get_username()
    password = get_password()
    
    # Authenticate user credentials
    user = User.authenticate(session, username, password)
    if user:
        return user
    else:
        # TODO: Implemente logic to handle wrong credentials
        #       Try again or Back to main menu ???
        ...
    
    
def log_in_user():
    """Logs in as a user"""

    # TODO: User login form with username and password before accessing the menu
    log_in_form()
    
    # Create user main menu object
    main_menu = Menu("User Menu", ["Search book", "Rent book", "Return book", "User information", "Exit"])
    
    # Display main menu and get user input
    while True:
        choice = main_menu.display()
        
        match choice:
            case "1":
                ...     #search_book()
            case "2":
                ...     #rent_book()
            case "3":
                ...     #return_book()
            case "4":
                ...     #user_information()
            case "5":
                sys.exit()
            case _:
                print("Invalid input")    


def log_in_admin():
    """Logs in as a administrator"""
    
    # TODO: User login form with username and password before accessing the menu
    log_in_form()
    
    # Create adminstrator main menu object
    admin_menu = Menu("Admin Menu", ["List rented books", "List available books", "Show balance", "Exit"])
    
    # Display admin menu and get user input
    while True:
        choice = admin_menu.display()
        
        match choice:
            case "1":
                ...     #list_rented_books()
            case "2":
                ...     #list_available_books()
            case "3":
                ...     #show_balance()
            case "4":
                sys.exit()
            case _:
                raise ValueError("Invalid input")
    
    
def main():
    """Main function"""
    
    # TODO: Initialize adminstrator accounts
    
    # Create init menu object
    init_menu = Menu("Library", ["Log-in", "Log-in as administrator", "Register user", "Exit"])
    
    # Display init menu and get user input
    while True:
        choice = init_menu.display()
        
        match choice:
            case "1":
                log_in_user()
            case "2":
                log_in_admin()
            case "3":
                register_user()
            case "4":
                sys.exit()
            case _:
                print("Invalid input")
    

if __name__ == "__main__":
    main()