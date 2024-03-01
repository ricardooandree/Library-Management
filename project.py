###################################################################################################
#######################################       IMPORTS       #######################################
###################################################################################################
import sys
import re

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
from tabulate import tabulate

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

# Create figlet object, set font and print menu title
figlet = Figlet()
figlet.setFont(font="slant")

###################################################################################################
#####################################       FUNCTIONS        ######################################
###################################################################################################
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

###################################################################################################
###################################       SEARCH BOOKS        #####################################
###################################################################################################
# TODO: ADD TESTS TRANSACTION CLASS
# TODO: ADD PASSWORD SAFETY REQUIREMENTS CHECK
# TODO: ONLY LOAD ADMIN ACCOUNTS/DATASET ONCE
# TODO: ADD TERMINAL CLEAR EVERY TIME IT ENTERS A MENU
# TODO: FINISH DOCSTRINGS

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
                return
            case _:
                print("Invalid input\n")
            
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
            print("ISBN cannot be empty\n")
            continue
        
        # Ensure input follows the format xxx-x-xx-xxxxxx-x
        parts = isbn.split('-')
        if len(parts) != 5 or not all(part.isdigit() for part in parts):
            print("ISBN must be of format xxx-x-xx-xxxxxx-x\n")
            continue
        
        # Validate length of each set of digits
        lengths = [3, 1, 2, 6, 1]
        valid = True
        for part, length in zip(parts, lengths):
            if len(part) != length:
                print(f"ISBN set must be a number of {length} digits\n")
                valid = False
        
        if not valid:
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
    
    
def rent_book(user):
    """Rent book"""
    
    # Print rent title
    print(figlet.renderText("Rent Book"))
    
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

###################################################################################################
####################################       RENT BOOK        #######################################
###################################################################################################
def return_book(user):
    """Return book"""
    
    # Print return title
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
#####################################       LISTING        ########################################
###################################################################################################
def list_books(_type=None):
    """List books by transaction type or all available books"""

    if _type:
        # Get all transaction objects in the database
        transactions = Transaction.get_all_type(session, transaction_type=_type)
        
        if not transactions:
            print("No transactions were found in the database\n")
            return
        
        # Get all book objects that have transaction information
        books = []
        for transaction in transactions:
            if transaction.get_status():
                books.append(Book.authenticate_id(session, transaction.get_book_id()))

        if books:
            Book.display_metadata(books)
        else:
            print("There are no active rented books\n")
            return
    else:
        # Get all available book objects
        books = Book.get_all_available(session)
        
        if books:
            Book.display_metadata(books)
        else:
            print("There are no available books\n")
            return
        
    
def list_transactions(_type=None, status=None):
    """List transactions by type or all transactions"""
    
    # Get all transaction objects in the database
    transactions = Transaction.get_all_type(session, transaction_type=_type)
    
    if not transactions:
        print("No transactions were found in the database\n")
        return
    
    # Get all books and users objects that have transaction information
    books, users = [], []
    for transaction in transactions:
        books.append(Book.authenticate_id(session, transaction.get_book_id()))
        users.append(User.authenticate_id(session, transaction.get_user_id()))
    
    # Get all book and user ids
    book_isbns = []
    for book in books:
        if book is not None:
            book_isbns.append(book.get_isbn())
        else: 
            book_isbns.append("Book doesn't exist anymore")
    
    user_usernames = []
    for user in users:
        if user is not None:
            user_usernames.append(user.get_username())
        else:
            user_usernames.append("User doesn't exist anymore")

    # Calls display method instance based on the listing request - by type or active rentals
    if status is None:
        Transaction.display(transactions, book_isbns, user_usernames)
    else:
        Transaction.display_active(transactions, book_isbns, user_usernames)
    

def list_users_fees():
    """List users total fees"""
    
    # Get users objects with total fees higher than 0
    users = User.get_all_fee(session)
    
    if users:
        User.display(users)
    else:
        print("There's no users with unpaid fees in the database\n")
        return

    
def admin_list_menu():
    """List admin menu"""
    
    # Create admin list menu object
    list_menu = Menu("List Menu", ["List available books", "List rented books", "List all transactions", "List rental transactions", "List return transactions", "List users total fees", "List active rentals", "Exit"])
    
    # Display admin list and get user input
    while True:
        choice = list_menu.display()
        
        match choice:
            case "1":
                list_books()
            case "2":
                list_books(_type="Rental")
            case "3":
                list_transactions()
            case "4":
                list_transactions(_type="Rental")
            case "5":
                list_transactions(_type="Return")
            case "6":
                list_users_fees()
            case "7":
                list_transactions(_type="Rental", status="active")
            case "8":
                return
            case _:
                print("Invalid input\n") 
                
###################################################################################################
####################################       SEARCHING        #######################################
###################################################################################################
def admin_search_user_transactions():
    """Displays all transactions made by a user"""
    
    # Get username input
    username = get_username()
    
    # Get user object by username
    user = User.authenticate_username(session, username)
    
    if user is None:
        print("There's no user registered in the database with that username\n")
        return
    
    # Get all transaction objects made by the user
    transactions = Transaction.get_all_username(session, user.get_id())
    
    if not transactions:
        print("No transactions made by user were found\n")
        return
    
    # Get all books objects that have transaction information
    books = []
    for transaction in transactions:
        books.append(Book.authenticate_id(session, transaction.get_book_id()))
    
    # Get all book and user ids
    book_isbns = []
    for book in books:
        if book is not None:
            book_isbns.append(book.get_isbn())
        else: 
            book_isbns.append("Book doesn't exist anymore")
    
    user_usernames = []
    for _ in range(len(transactions)):
        user_usernames.append(username)
    
    # Print all user transactions
    Transaction.display(transactions, book_isbns, user_usernames)
    
    
def admin_search_book_transactions():
    """Displays all transactions corresponding to a book"""
    
    # Get isbn input
    isbn = get_isbn()
    
    # Get book object by isbn
    book = Book.authenticate_isbn(session, isbn)

    if book is None:
        print("There's no book registered in the database with that ISBN\n")
        return
    
    # Get all transaction objects made for the book
    transactions = Transaction.get_all_isbn(session, book.get_id())
    
    if not transactions:
        print("No transactions for that book were found\n")
        return
    
    # Get all users objects that have transaction information
    users = []
    for transaction in transactions:
        users.append(User.authenticate_id(session, transaction.get_user_id()))
    
    # Get all book and user ids
    user_usernames = []
    for user in users:
        if user is not None:
            user_usernames.append(user.get_username())
        else: 
            user_usernames.append("User doesn't exist anymore")
    
    book_isbns = []
    for _ in range(len(transactions)):
        book_isbns.append(isbn)
    
    # Print all book transactions
    Transaction.display(transactions, book_isbns, user_usernames)
    

def admin_searching_menu():
    """Search admin menu"""
    
    # Create admin search menu object
    search_menu = Menu("Search Menu", ["Search user transactions", "Search book transactions", "Exit"])
    
    # Display admin search menu and get user input
    while True:
        choice = search_menu.display()
        
        match choice:
            case "1":
                admin_search_user_transactions()
            case "2":
                admin_search_book_transactions()
            case "3":
                return
            case _:
                print("Invalid input\n")
                
###################################################################################################
#################################       ADD/REMOVE BOOK        ####################################
###################################################################################################
def get_description():
    """Get description input from the user"""
    
    # Get user description
    while True:
        print("Usage example: Young wizard Harry Potter receives his invitational letter to study at Hogwarts\n")
        
        # Get user input
        description = input("Enter description: ")
        
        if not description:
            print("Description cannot be empty\n")
            continue
        
        if not description[0].isalpha() or not description[-1].isalpha():
            print("Description must not start or end with non-alpha characters\n")
            continue
        
        if len(description) > 500:
            print("Description must be a maximum of 500 characters")
            continue
        
        # Return valid description
        return description
    
    
def admin_add_book():
    """Adds a book to the database"""
    
    # Get isbn attribute input 
    isbn = get_isbn()
    
    # Validates if the already book exists
    existing_book = Book.authenticate_isbn(session, isbn)
    
    if existing_book is None:
        # Get other book attributes input
        title = get_title()
        author = get_author()
        publisher = get_publisher()
        genre = get_genre()
        edition = get_edition()
        publication_date = get_publication_date()
        description = get_description()
        price = get_price()
        
        # Register the book
        Book.register(session, title, author, publisher, genre, edition, publication_date, description, price, isbn)
        print("Successfully registered a new book in the database\n")
        
    else:
        # Adds copy of the book
        Book.add(session, existing_book)
        print("Succesfully added a new book in the database\n")


def admin_remove_book():
    """Removes a book from the database"""
    
    # Get isbn attribute input 
    isbn = get_isbn()
    
    # Validates if the already book exists
    existing_book = Book.authenticate_isbn(session, isbn)
    
    if existing_book:
        # Get on going rental transactions for that specific book
        transactions = Transaction.authenticate_book_id(session, existing_book.get_id(), type="Rental")
        
        # If there's no available books for renting and there's at least one currently rented can't remove the book
        if existing_book.get_quantity() == 0 and transactions:
            print("There are currently no ongoing rentals for that book, can't remove the book from the database\n")
            return
        
        # If there's available books for renting then can remove one book
        if existing_book.get_quantity() > 0:
            # Remove the book
            Book.remove(session, existing_book)
            print("Succesfully removed the book in the database\n")
            return
        
        if existing_book.get_quantity() == 0 and not transactions:
            # Delete the book from the database
            Book.delete(session, existing_book)
            print("Succesfully deleted the book in the database\n")
            return
        
    else:
        print("The book does not exist in the database\n")
        

###################################################################################################
##################################       SHOW BALANCE        ######################################
###################################################################################################
def admin_show_balance():
    """Display library's balance"""
    
    # Get all transaction objects with of type Return
    transactions = Transaction.get_all_type(session, transaction_type="Return")
    
    # Library's balance
    balance = 0.0
    for transaction in transactions:
        balance += transaction.get_fee()
        
    # Print balance
    headers = ["Balance"]
    table = [[balance]]
    
    print(tabulate(table, headers, tablefmt="double_outline"))

###################################################################################################
################################       LOGIN/REGISTRATION        ##################################
###################################################################################################
def get_username():
    """Get username input from the user"""
    
    while True:
        # Get username input
        username = input("Enter username: ")
        
        # Check if username is empty
        if not username:
            print("Username cannot be empty\n")
            continue
        
        # Check if username is more than 50 characters long
        if len(username) > 50:
            print("Username must be less than 50 characters long\n")
            continue
        
        # Regular expression pattern allowing alphanumeric characters and specified special characters
        pattern = r'^[a-zA-Z0-9_-]+$'
        
        # Match the input string against the pattern
        if not re.match(pattern, username):
            print("Username, can't contain spaces or special characters that are not - or _")
            continue

        # Return valid username
        return username
            
            
def get_password():
    """Get password input from the user"""
    
    while True:
        # Get user password
        password = input("Enter password: ")
        
        # Check if password is empty
        if not password:
            print("Password cannot be empty\n")
            continue
        
        # Check if password is more than 50 characters long
        if len(password) > 50:
            print("Password must be less than 50 characters long\n")
            continue
        
        # Check if password contains spaces
        if ' ' in password:
            print("Password cannot contain spaces\n")
            continue
        
        # Return valid password
        return password
            

def get_password_confirm():
    """Get password confirmation input from the user"""
    
    while True:
        # Get user password
        password_confirm = input("Enter password confirmation: ")
        
        # Check if password confirmation is empty
        if not password_confirm:
            print("Password cannot be empty\n")
            continue
        
        # Check if password confirmation is more than 50 characters long
        if len(password_confirm) > 50:
            print("Password must be less than 50 characters long\n")
            continue
        
        # Check if password confirmation contains spaces
        if ' ' in password_confirm:
            print("Password cannot contain spaces\n")
            continue
        
        # Return valid password confirmation
        return password_confirm
            

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
    

def register():
    """Register user"""
    
    # Calls user registration form and handles the registration validation
    user = register_form()

    # Check if user is admin or not and displays the corresponding menu
    if user.get_is_admin():
        admin_menu(user)
    else:
        user_menu(user)
    

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
          
    
def admin_menu():
    """Displays admin menu"""
    
    # Create admin main menu object
    admin_menu = Menu("Admin Menu", ["Listing", "Search", "Add book", "Remove Book", "Show balance", "Exit"])
    
    # Display admin menu and get user input
    while True:
        choice = admin_menu.display()
        
        match choice:
            case "1":
                admin_list_menu()
            case "2":
                admin_searching_menu()
            case "3":
                admin_add_book()
            case "4":
                admin_remove_book()
            case "5":
                admin_show_balance()
            case "6":
                sys.exit()
            case _:
                print("Invalid input\n") 


def user_menu(user):
    """Displays user menu"""
    # Create user main menu object
    user_menu = Menu("User Menu", ["Search book", "Rent book", "Return book", "User information", "Exit"])
    
    # Display main menu and get user input
    while True:
        choice = user_menu.display()
        
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
                print("Invalid input\n")


def log_in():
    """Logs in"""

    # Calls user login form and handles the login authentication
    user = log_in_form()

    # Check if user is admin or not and displays the corresponding menu
    if user.get_is_admin():   
        admin_menu()
    else:  
        user_menu(user)
        
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
                log_in()
            case "2":
                register()
            case "3":
                sys.exit()
            case _:
                print("Invalid input\n")
          
                
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