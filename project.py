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
# FIXME: REDIRECTING TO MAIN MENU
# FIXME: BETTER USER INPUT VALIDATION
def get_title():
    """Get title input from the user"""
    
    # Get user title
    while True:
        print("Usage example: OOP Python Fundamentals")
        
        title = input("Enter title: ")
        
        # Ensures input is not an empty string
        if title:
            return title
        else:
            print("Invalid title\n")
            
            
def get_author():
    """Get author input from the user"""
    
    # Get user author
    while True:
        print("Usage example: Ricardo Silva")
        
        author = input("Enter author: ")
        
        # Ensures input is not an empty string
        if author:
            return author
        else:
            print("Invalid author name\n")
            
            
def get_publisher():
    """Get publisher input from the user"""
    
    # Get user publisher
    while True:
        print("Usage example: HarperCollins")
        
        publisher = input("Enter publisher: ")
        
        # Ensures input is not an empty string
        if publisher:
            return publisher
        else:
            print("Invalid publisher\n")
            
            
def get_genre():
    """Get genre input from the user"""
    
    # Get user author
    while True:
        print("Usage example: Educational")
        
        genre = input("Enter genre: ")
        
        # Ensures input is not an empty string
        if genre:
            return genre
        else:
            print("Invalid genre\n")
            
       
def get_edition():
    """Get edition input from the user"""
    
    # Get user edition
    while True:
        print("Usage example: 1")
        
        # Ensures input is an integer value higher than zero
        try: 
            edition = int(input("Enter edition: "))

            if edition > 0:
                return edition
        except ValueError:
            print("Invalid edition\n")
            

def get_publication_date():
    """Get publication date input from the user"""
    
    # Get user publication date
    while True:
        print("Usage example: 25-02-2024")
        
        # Ensures input is of type dd-mm-yyyy and each element is between expected real values
        try:
            publication_date = input("Enter publication date: ")
            
            day, month, year = map(int, publication_date.split('-'))
            
            if not 1 <= day <= 31:
                print("Invalid day\n")
                continue
            
            elif not 1 <= month <= 12:
                print("Invalid month\n")
                continue
                
            elif not 1800 <= year <= 2100:
                print("Invalid year\n")
                continue
                
            return publication_date
            
        except ValueError:
            print("Invalid publication date\n")


def get_price():
    """Get price input from the user"""
    
    # Get user price
    while True:
        print("Usage example: 9.99")
        
        # Ensures input if float higher than zero
        try:
            price = float(input("Enter price: "))

            if price > 0:
                return price
        except ValueError:
            print("Invalid price\n")
            

def search_by_title():
    """Searches book by title, gets user input and handles validation cases"""
    
    # Get user title input
    title = get_title()
    
    # Authenticates book title by validating the title and searching for books with that title in the database
    books = Book.authenticate_title(session, title)
    if books:
        Book.display_metadata(books)
    else:
        print("The library doesn't own any book with that title\n")
        # TODO: Redirects to main menu
        
        
def search_by_author():
    """Searches books by author, gets user input and handles validation cases"""
    
    # Get user author input
    author = get_author()
    
    # Authenticates book author by validating the author and searching for it in the database
    books = Book.authenticate_author(session, author)
    if books:
        Book.display_metadata(books)
    else:
        print("The library doesn't own any books of that author\n")
        # TODO: Redirects to main menu
        

def search_by_publisher():
    """Searches books by publisher, gets user input and handles validation cases"""
    
    # Get user publisher input
    publisher = get_publisher()
    
    # Authenticates book publisher by validating the publisher and searching for it in the database
    books = Book.authenticate_publisher(session, publisher)
    if books:
        Book.display_metadata(books)
    else:
        print("The library doesn't own any books of that publisher\n")
        # TODO: Redirects to main menu
        
        
def search_by_genre():
    """Searches books by genre, gets user input and handles validation cases"""
    
    # Get user genre input
    genre = get_genre()
    
    # Authenticates book genre by validating the genre and searching for it in the database
    books = Book.authenticate_genre(session, genre)
    if books:
        Book.display_metadata(books)
    else:
        print("The library doesn't own any books of that genre\n")
        # TODO: Redirects to main menu
    

def search_by_edition():
    """Searches books by edition, gets user input and handles validation cases"""
    
    # Get user edition input
    edition = get_edition()
    
    # Authenticates book edition by validating the edition and searching for it in the database
    books = Book.authenticate_edition(session, edition)
    if books:
        Book.display_metadata(books)
    else:
        print("The library doesn't own any books of that edition\n")
        # TODO: Redirects to main menu
        

def search_by_publication_date():
    """Searches books by publication date, gets user input and handles validation cases"""
    
    # Get user publication date input
    publication_date = get_publication_date()
    
    # Authenticates book publication date by validating the publication date and searching for it in the database
    books = Book.authenticate_publication_date(session, publication_date)
    if books:
        Book.display_metadata(books)
    else:
        print("The library doesn't own any books of that publication date\n")
        # TODO: Redirects to main menu
        

def search_by_price():
    """Searches books by price, gets user input and handles validation cases"""
    
    # Get user price input
    price = get_price()
    
    # Authenticates book price by validating the price and searching for it in the database
    books = Book.authenticate_price(session, price)
    if books:
        Book.display_metadata(books)
    else:
        print("The library doesn't own any books of that price\n")
        # TODO: Redirects to main menu
        
        
def search_book():
    """Search book"""
    
    # Create search book menu object
    search_book_menu = Menu("Search Book", ["Search by title", "Search by author", "Search by publisher", "Search by genre", "Search by edition", "Search by publication date", "Search by price", "Exit"])
    
    # Display search book menu and get user input
    while True:
        choice = search_book_menu.display()
        
        match choice:
            case "1":
                search_by_title()
            case "2":
                search_by_author()
            case "3":
                search_by_publisher()
            case "4":
                search_by_genre()
            case "5":
                search_by_edition()
            case "6":
                search_by_publication_date()
            case "7":
                search_by_price()
            case "8":
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

    # TODO: Calls main menu
    

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
        # TODO: Add book, remove book
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
    
    # Load admin accounts into the database
    load_admin_accounts(session, "admin_accounts.json")
    
    # Load books into the database
    load_books(session, "books_test.json")
    
    # Calls init menu to be displayed
    init_menu()
    

if __name__ == "__main__":
    main()