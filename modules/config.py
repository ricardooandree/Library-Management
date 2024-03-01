###################################################################################################
#######################################       IMPORTS       #######################################
###################################################################################################
import json
from modules.user import User
from modules.book import Book
from modules.transaction import Transaction
from datetime import datetime
###################################################################################################
#####################################       FUNCTIONS        ######################################
###################################################################################################
def load_admin_accounts(session, file_path):
    """Loads the admin accounts from the json file"""
    
    # Opens configuration file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Gets the list of admin accounts
    admin_accounts = data.get("admins", [])
    
    for admin in admin_accounts:
        # Validates if the admin account doesn't exist
        if User.validate(session , admin['username'], admin['password'], admin['password']):
            # Register admin account
            User.register(session, admin['username'], admin['password'], admin=True)
            

def load_books(session, file_path):
    """Loads the books from the json file"""
    
    # Opens configuration file
    with open(file_path, 'r') as file:
        data = json.load(file)
        
    # Gets the list of books
    books = data.get("books", [])
    
    for book in books:
        # Validates if the book exists
        existing_book = Book.authenticate_isbn(session, book['isbn'])
        if existing_book is None:
            # Register book
            Book.register(session, book['title'], book['author'], book['publisher'], book['genre'], book['edition'], book['publication_date'], book['description'], book['price'], book['isbn'])
        else:
            # Adds copy of the book
            Book.add(session, existing_book)
    
    
def load_transactions(session, file_path):
    """Load the transactions from the json file"""
    # Opens configuration file
    with open(file_path, 'r') as file:
        data = json.load(file)
        
    # Gets the list of transactions
    transactions = data.get("transactions", [])
    
    for transaction in transactions:
        # Convert date strings to datetime.date objects
        checkout_date = datetime.strptime(transaction['checkout_date'], '%Y-%m-%d').date()
        return_date = datetime.strptime(transaction['return_date'], '%Y-%m-%d').date()
        
        # Registers transaction
        Transaction.register(session, transaction['user_id'], transaction['book_id'], checkout_date, return_date, transaction['fee'], transaction['status'], transaction['type'])
