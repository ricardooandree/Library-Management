###################################################################################################
#######################################       IMPORTS       #######################################
###################################################################################################
import os
import sys
import random 

from modules.user import Base
from modules.menu import Menu
from modules.user import User
from modules.book import Book
from modules.transaction import Transaction
from modules.config import load_admin_accounts, load_books
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

###################################################################################################
###################################       SEARCH BOOKS        #####################################
###################################################################################################
def get_title():
    """Get title input from the user"""
    
    # Get user title
    while True:
        title = input("Enter title: ")
        if title:
            return title
        else:
            print("Please enter title\n")
            
            
def search_by_title():
    """Search book by title, gets user input and handles validation cases"""
    
    # Get user title input
    title = get_title()
    
    # Authenticates book title by validating the title and searching for it in the database
    book = Book.authenticate_title(session, title)
    if book:
        book.display_metadata()
    else:
        print("Invalid title or the library doesn't own the book\n")
        # TODO: Redirects to main menu
        
        
def search_book():
    """Search book"""
    
    # Create search book menu object
    search_book_menu = Menu("Search Book", ["Search by title", "Search by author", "Search by genre", "Search by publication date", "Exit"])
    
    # Display search book menu and get user input
    while True:
        choice = search_book_menu.display()
        
        match choice:
            case "1":
              search_by_title()
            case "2":
              ...     #search_by_author()
            case "3":
              ...     #search_by_genre()
            case "4":
              ...     #search_by_publication_date()
            case "5":
                sys.exit()
            case _:
                raise ValueError("Invalid input")
            
###################################################################################################
################################       LOGIN/REGISTRATION        ##################################
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
    
    # Get user registration input
    username = get_username()
    password = get_password()
    password_confirm = get_password_confirm()
    
    # Validate credentials
    if User.validate(session, username, password, password_confirm):
        # Register user
        return User.register(session, username, password)
    else:
        # NOTE: Current implementation: wrong credentials -> redirects to initial menu
        print("User already exists or password doesn't match password confirmation\n")
        init_menu()
    

def register_user():
    """Register user"""
    
    # Calls user registration form and handles the registration validation
    user = register_form()

    # TODO: Display main menu


def log_in_form():
    """Log in form, gets user input, validates it and handles validation cases"""
    
    # Get user login input
    username = get_username()
    password = get_password()
    
    # Authenticate user credentials
    user = User.authenticate(session, username, password)
    if user:
        return user
    else:
        # NOTE: Current implementation: wrong credentials -> redirects to initial menu
        print("Wrong credentials\n")
        init_menu()
          
    
# FIXME: Implement user menu and admin menu on an auxiliar function
def log_in_user():
    """Logs in as a user"""

    # Calls user login form and handles the login authentication
    user = log_in_form()

    # Check if user is admin or not and displays the corresponding menu
    if user.get_is_admin():   
        # Create admin main menu object
        main_menu = Menu("Admin Menu", ["List rented books", "List available books", "Show balance", "Exit"])
        
        # Display admin menu and get user input
        while True:
            choice = main_menu.display()
            
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
    else:  
        # Create user main menu object
        main_menu = Menu("User Menu", ["Search book", "Rent book", "Return book", "User information", "Exit"])
        
        # Display main menu and get user input
        while True:
            choice = main_menu.display()
            
            match choice:
                case "1":
                    search_book()
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
        

###################################################################################################
################################       INITIALIZATION/MAIN        #################################
###################################################################################################
def init_menu():
    """Display the initial menu"""
    
    # Create init menu object
    init_menu = Menu("Library", ["Log-in", "Register", "Exit"])
    
    # Display init menu and get user input
    while True:
        choice = init_menu.display()
        
        match choice:
            case "1":
                log_in_user()
            case "2":
                register_user()
            case "3":
                sys.exit()
            case _:
                print("Invalid input")
          
                
def main():
    """Main function"""
    
    # Load admin accounts
    load_admin_accounts(session, "admin_accounts.json")
    
    # Load books
    load_books(session, "books.json")
    
    # Calls init menu to be displayed
    init_menu()
    

if __name__ == "__main__":
    main()