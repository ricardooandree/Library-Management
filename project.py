###################################################################################################
#######################################       IMPORTS       #######################################
###################################################################################################
import os
import sys
import random 

from modules.menu import Menu
from modules.user import User
from modules.book import Book
from modules.transaction import Transaction
from werkzeug.security import check_password_hash, generate_password_hash

###################################################################################################
#################################       APP CONFIGURATION        ##################################
###################################################################################################


###################################################################################################
#####################################       FUNCTIONS        ######################################
###################################################################################################

    
        
def register_form():
    """Register form"""
    
    # Get user username FIXME: Needs verification loop + validation
    username = input("Enter username: ").strip()
    if not username:
        raise ValueError("Please enter username")
    
    # TODO: Check if username already exists
    
    # Get user password FIXME: Needs verification loop + validation
    password = input("Enter password: ").strip()
    if not password:
        raise ValueError("Please enter password")
    
    # Get user password confirmation FIXME: Needs verification loop + validation
    password_confirm = input("Enter password: ").strip()
    if not password_confirm:
        raise ValueError("Please enter password confirmation")
    
    # TODO: Check if password matches password_confirm 
    # TODO: Check if password is safe enough
    # TODO: Register user - Add user to the table 
    # NOTE: Return True if valid?
    


def register_user():
    """Register user"""
    
    # TODO: User register form with username and password before accessing the menu
    register_form()
    
    
def log_in_form():
    """Log in form"""
    
    # TODO: Create user object
    # user = User()
    
    # Get user username FIXME: Needs verification loop + validation
    username = input("Enter username: ").strip()
    if not username:
        raise ValueError("Please enter username")
    
    # TODO: Check if username exists
    
    # Get user password FIXME: Needs verification loop + validation
    password = input("Enter password: ").strip()
    if not password:
        raise ValueError("Please enter password")
    
    # TODO: Check if password is correct
    # NOTE: Return True if valid?
    
    
def log_in_user():
    """Logs in as a user"""

    # TODO: User login form with username and password before accessing the menu
    
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
    
    # Create adminstrator main menu object
    init_menu = Menu("Admin Menu", ["List rented books", "List available books", "Show balance", "Exit"])
    
    # Display admin menu and get user input
    while True:
        choice = init_menu.display()
        
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
    init_menu = Menu("Library", ["Log-in as user", "Log-in as administrator", "Register user", "Exit"])
    
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