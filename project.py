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
from datetime import datetime, timedelta
from pyfiglet import Figlet
###################################################################################################
#################################       APP CONFIGURATION        ##################################
###################################################################################################
# Initialize the SQLAlchemy engine for sqlite
engine = create_engine('sqlite:///library.db')  # Adjust the database URL as needed

# Create the Base tables for each class
Base.metadata.create_all(engine)

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
# FIXME: REDIRECTING TO MAIN MENU / REDIRECTS IN GENERAL
# FIXME: MENUS NO OPTION -> NOT RAISEVALUE BUT CONTINUE + PRINT MESSAGE
# FIXME: IMPLEMENT MENUS IN AUXILIAR FUNCTION
# NOTE: FEE FOR LATE RETURN - TRANSACTION LATE RETURN? 
# TODO: ADD BETTER VALIDATION FOR SETTERS IN USER 
# TODO: ADD BETTER VALIDATION FOR SETTERS IN TRANSACTION 
# TODO: ADD TESTS USER CLASS
# TODO: ADD TESTS TRANSACTION CLASS
def basic_string_attribute_validation(string, attribute):
    # Basic string attribute validation
    if not isinstance(string, str):
        return f"{attribute} must be a string\n"
    
    if not string:
        return f"{attribute} cannot be empty\n"
    
    if not string[0].isalpha() or not string[-1].isalpha():
        return f"{attribute} must not start or end with non-alphabetical characters\n"
    
    if len(string) > 100:
        return f"{attribute} must have a maximum of 100 characters\n"
    
    # Valid string
    return True


def get_title():
    """Get title input from the user"""
    
    while True:
        print("Usage example: OOP Python Fundamentals")
        
        # Get user input
        title = input("Enter title: ")
        
        # Call auxiliar function to validate basic string attribute features
        validation_result = basic_string_attribute_validation(title, attribute="Title")
        
        if isinstance(validation_result, str):
            print(validation_result)
            continue
        
        # Return valid title
        return title
            
            
def get_author():
    """Get author input from the user"""
    
    # Get user author
    while True:
        print("Usage example: Ricardo Silva")
        
        # Get user input
        author = input("Enter author: ")
        
        # Call auxiliar function to validate basic string attribute features
        validation_result = basic_string_attribute_validation(author, attribute="Author")
        
        if isinstance(validation_result, str):
            print(validation_result)
            continue
        
        # Return valid author
        return author
            
            
def get_publisher():
    """Get publisher input from the user"""
    
    # Get user publisher
    while True:
        print("Usage example: HarperCollins")
        
        # Get user input
        publisher = input("Enter publisher: ")
        
        # Call auxiliar function to validate basic string attribute features
        validation_result = basic_string_attribute_validation(publisher, attribute="Publisher")
        
        if isinstance(validation_result, str):
            print(validation_result)
            continue
        
        # Return valid publisher
        return publisher
            
            
def get_genre():
    """Get genre input from the user"""
    
    # Get user author
    while True:
        print("Usage example: Educational")
        
        # Get user input
        genre = input("Enter genre: ")
        
        # Call auxiliar function to validate basic string attribute features
        validation_result = basic_string_attribute_validation(genre, attribute="Genre")
        
        if isinstance(validation_result, str):
            print(validation_result)
            continue
            
       
def get_edition():
    """Get edition input from the user"""
    
    # Get user edition
    while True:
        print("Usage example: 1")
        
        # Validates edition attribute - must be a positive integer
        try: 
            edition = int(input("Enter edition: "))
        
        except ValueError:
            print("Edition must be an integer\n")
            continue
        
        if edition <= 0:
            print("Edition must be a positive integer\n")
            continue
        
        # Return valid edition
        return edition
            

def get_publication_date():
    """Get publication date input from the user"""
    
    # Get user publication date
    while True:
        print("Usage example: 25-02-2024")
        
        # Get user input
        publication_date = input("Enter publication date: ")
        
        # Ensure input is not empty
        if not publication_date:
            print("Publication date cannot be empty\n")
            continue
            
        # Ensure input follows the format dd-mm-yyyy
        if len(publication_date) != 10 or publication_date.count('-') != 2:
            print("Publication date must be of format dd-mm-yyyy\n")
            continue
    
        # Split the input after initial checks
        day, month, year = publication_date.split('-')
        
        # Validate day, month, and year components
        if not (day.isdigit() and month.isdigit() and year.isdigit()):
            print("Publication date components must be integers\n")
            continue
        
        day, month, year = int(day), int(month), int(year)

        if not 1 <= day <= 31:
            print("Publication date day must be in between 1 and 31\n")
            continue
            
        if not 1 <= month <= 12:
            print("Publication date month must be in between 1 and 12\n")
            continue
        
        if not 1800 <= year <= 2100:
            print("Publication date year must be in between 1800 and 2100\n")
            continue
        
        # Return valid publication date
        return publication_date


def get_price():
    """Get price input from the user"""
    
    # Get user price
    while True:
        print("Usage example: 9.99")
        
        # Validates edition attribute - must be a positive float
        try:
            price = float(input("Enter price: "))
        except ValueError:
            print("Edition must be of type float\n")
            continue
        
        if price <= 0.0:
            print("Edition must be a positive float number\n")
            continue
        
        # Return valid price
        return price
            

def show_all_books():
    """Displays all books in the database"""
    
    # Get all books from the database
    books = Book.get_all(session)
    if books:
        Book.display_metadata(books)
    else:
        print("The library doesn't own any books\n")
        # TODO: Redirects to main menu


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
    search_book_menu = Menu("Search Book", ["Show all books", "Search by title", "Search by author", "Search by publisher", "Search by genre", "Search by edition", "Search by publication date", "Search by price", "Exit"])
    
    # Display search book menu and get user input
    while True:
        choice = search_book_menu.display()
        
        match choice:
            case "1":
                show_all_books()
            case "2":
                search_by_title()
            case "3":
                search_by_author()
            case "4":
                search_by_publisher()
            case "5":
                search_by_genre()
            case "6":
                search_by_edition()
            case "7":
                search_by_publication_date()
            case "8":
                search_by_price()
            case "9":
                sys.exit()
            case _:
                raise ValueError("Invalid input")
            
###################################################################################################
####################################       RENT BOOK        #######################################
###################################################################################################
def get_isbn():
    """Get ISBN input from the user and handles validation"""
    
    # Get user ISBN
    while True:
        print("Usage example: 111-2-33-444444-5")
        
        isbn = input("Enter ISBN: ").strip()
        
        # Ensure input is not empty
        if not isbn:
            print("Publication date cannot be empty\n")
            continue
        
        # Ensure input follows the format xxx-x-xx-xxxxxx-x
        parts = isbn.split('-')
        if len(parts) != 5 or not all(part.isdigit() for part in parts):
            print("ISBN must be of format xxx-x-xx-xxxxxx-x")
            continue
        
        # Validate length of each set of digits
        lengths = [3, 1, 2, 6, 1]
        for part, length in zip(parts, lengths):
            if len(part) != length:
                print(f"ISBN set must be a number of {length} digits")
                continue
            
        # Return valid ISBN
        return isbn
            

def get_return_date():
    """Get return date input from the user"""
    
    # Get user return date
    while True:
        print("\nUsage example: 27-02-2024")
        
        # Validates return date attribute - must be a valid date
        try:
            return_date = datetime.strptime(input("Enter return date: "), "%d-%m-%Y").date()
        except ValueError:
            print("Return date must be of type date\n")
            continue
        
        # Get current date
        current_date = datetime.now().date()
        
        # Check if return date is in the past 
        if return_date <= current_date:
            print("Return date must be a valid date in the future\n")
            continue
        
        # Check if return date is more than 30 days from the current date
        if return_date > current_date + timedelta(days=30):
            print("Return date must be within 30 days from today\n")
            continue
        
        # Return valid return date
        return return_date, current_date
    
    
def rent_specific_book(user):
    """Rent specific book"""
    
    # Get user ISBN input
    isbn = get_isbn()
    
    # Authenticates book isbn by validating the isbn and searching for it in the database
    book = Book.authenticate_isbn(session, isbn)
    
    if book is None:
        print("The library doesn't own the specified book\n")
        return
    
    # Check if the book is available for renting and if the user is authorized to rent it
    if book.get_quantity() == 0:
        print("The library doesn't currently have the specified book available for renting\n")
        return
     
    if user.get_total_fee() >= 100.0:
        print("Failed to rent book, the user's currently total fee amount is over $100\n")
        return

    # Check if user has an active rental transaction for the specified book
    transactions = Transaction.authenticate_user_book(session, user.get_id(), book.get_id(), type="Rental")
    
    if transactions is not None:
        for transaction in transactions:
            if transaction.get_status():
                print("Failed to rent book, the library only allows 1 copy of the same book per person\n")
                return
    
    # Get user return date input
    return_date, checkout_date = get_return_date()
    
    # Book rent book method - update quantity
    book.rent_book(session)
    
    # Get renting book fee for the specified time duration
    fee = book.calculate_fee(return_date, checkout_date)

    # User rent book method - update total_fee
    user.rent_book(session, fee)

    # Registers new rental transaction
    if not Transaction.register(session, user.get_id(), book.get_id(), checkout_date, return_date, fee, status=True, type="Rental"):
        print("Failed to register transaction\n")
        return
    
    print("Successfully registered book rental\n")


def rent_book(user):
    """Rent book"""
    # Create rent book menu object
    rent_book_menu = Menu("Rent Book", ["Show all books", "Rent book", "Exit"])
    
    # Display rent book menu and get user input
    while True:
        choice = rent_book_menu.display()
        
        match choice:
            case "1":
                show_all_books()
            case "2":
                rent_specific_book(user)
            case "3":
                sys.exit()
            case _:
                raise ValueError("Invalid input")

###################################################################################################
####################################       RENT BOOK        #######################################
###################################################################################################
def return_book(user):
    """Return book"""
    # Create figlet object, set font and print menu title
    figlet = Figlet()
    figlet.setFont(font="slant")
    print(figlet.renderText("Return Book"))
    
    # Get ISBN user input
    isbn = get_isbn()
    
    # Authenticates book isbn by validating the isbn and searching for it in the database
    book = Book.authenticate_isbn(session, isbn)
    
    if book is None:
        print("The library doesn't own the specified book\n")
        return
    
    # Check if user has an active rental transaction for the specified book
    transactions = Transaction.authenticate_user_book(session, user.get_id(), book.get_id(), type="Rental")
    
    # Check if user has any rental transactions
    if transactions is None:
        print("The user has not rented the specified book\n")
        return
    
    # Check if the user has any active rental transaction 
    target_transaction = None
    for transaction in transactions:
        if transaction.get_status():
            target_transaction = transaction
            break
    
    if target_transaction is None:
        print("The user has not rented the specified book\n")
        return
    
    # Get current date
    current_date = datetime.now().date()
    
    # Get return_date from transaction
    return_date = target_transaction.get_return_date()
    
    # Get fee from transaction
    fee = target_transaction.get_fee()
    
    # Check if the return is early, late or on time
    if current_date < return_date:
        _type = "Early Return"
    
    elif current_date > return_date:
        _type = "Late Return"
        fee += 50.0
        
    else:
        _type = "Return"
    
    # Book return book method - update quantity
    book.return_book(session)
    
    # User return book method - update total_fee
    user.return_book(session, fee)
    
    # Update rental transaction status
    target_transaction.set_status(False)
    
    # Registers new return transaction
    if not Transaction.register(session, user.get_id(), book.get_id(), target_transaction.get_checkout_date(), current_date, fee, status=False, type=_type):
        print("Failed to register transaction\n")
        return

    print("Successfully registered book return\n")
    
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
          
    
def log_in_user():
    """Logs in as a user"""

    # Calls user login form and handles the login authentication
    user = log_in_form()

    # Check if user is admin or not and displays the corresponding menu
    if user.get_is_admin():   
        # Create admin main menu object
        # NOTE: Add book, remove book
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
                    rent_book(user)
                case "3":
                    return_book(user)
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
    load_books(session, "books.json")
    
    # Calls init menu to be displayed
    init_menu()
    

if __name__ == "__main__":
    main()