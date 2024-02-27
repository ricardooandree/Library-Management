###################################################################################################
#######################################       IMPORTS       #######################################
###################################################################################################
import sys
import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add the parent directory (Library-Management) to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.user import Base
from modules.book import Book
from modules.config import load_books
###################################################################################################
####################################       CONFIGURATION       ####################################
###################################################################################################
# Initialize the SQLAlchemy engine for sqlite
engine = create_engine('sqlite:///test_book.db')  # Adjust the database URL as needed

# Create the Base tables for each class
Base.metadata.create_all(engine)

# Create a Session class and bind the engine to it
Session = sessionmaker(bind=engine)

# Create session object
session = Session()

# Load books into the test database
load_books(session, "books_test.json")
###################################################################################################
################################       SETTER/GETTER TESTS       ##################################
###################################################################################################
def test_valid_title():
    # Test valid title input
    book = Book()
    valid_title = "OOP Python Fundamentals"
    book.set_title(valid_title)
    assert book.get_title() == valid_title

def test_invalid_title():
    # Test invalid author input
    book = Book()
    invalid_title = ""  # Empty string
    with pytest.raises(ValueError):
        book.set_title(invalid_title)
        
    invalid_title = 1  # Not a string
    with pytest.raises(ValueError):
        book.set_title(invalid_title)
        
    invalid_title = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla nec velit nec leo mattis fermentum eget ut magna. Sed tincidunt justo ut ultricies feugiat"  # String bigger than 100 characters
    with pytest.raises(ValueError):
        book.set_title(invalid_title)
    
    invalid_title = " OOP Python Fundamentals " # Leading and trailing spaces
    with pytest.raises(ValueError):
        book.set_title(invalid_title)
        
    invalid_title = "1OOP Python Fundamentals1" # Does not start or end with alphabetic characters
    with pytest.raises(ValueError):
        book.set_title(invalid_title)
    
    invalid_title = "!OOP Python Fundamentals," # Does not start or end with alphabetic characters
    with pytest.raises(ValueError):
        book.set_title(invalid_title)
           
def test_valid_author():
    # Test valid author input
    book = Book()
    valid_author = "Ricardo Silva"
    book.set_author(valid_author)
    assert book.get_author() == valid_author
    
def test_invalid_author():
    # Test invalid author input
    book = Book()
    invalid_author = ""  # Empty string
    with pytest.raises(ValueError):
        book.set_author(invalid_author)
        
    invalid_author = 1  # Not a string
    with pytest.raises(ValueError):
        book.set_author(invalid_author)
        
    invalid_author = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla nec velit nec leo mattis fermentum eget ut magna. Sed tincidunt justo ut ultricies feugiat"  # String bigger than 100 characters
    with pytest.raises(ValueError):
        book.set_author(invalid_author)
    
    invalid_author = " Ricardo Silva " # Adds leading and trailing spaces
    with pytest.raises(ValueError):
        book.set_author(invalid_author)
        
    invalid_author = "1Ricardo Silva1" # Does not start or end with alphabetic characters
    with pytest.raises(ValueError):
        book.set_author(invalid_author)
    
    invalid_author = "!Ricardo Silva," # Does not start or end with alphabetic characters
    with pytest.raises(ValueError):
        book.set_author(invalid_author)
    
    invalid_author = "RicardoSilva"  # Missing space between first and last name
    with pytest.raises(ValueError):
        book.set_author(invalid_author)
    
    invalid_author = "Ricardo-Silva"  # Missing space between first and last name
    with pytest.raises(ValueError):
        book.set_author(invalid_author)
        
    invalid_author = "Ricardo Andre Silva" # Adds extra name
    with pytest.raises(ValueError):
        book.set_author(invalid_author)
         
def test_valid_publisher():
    # Test valid publisher input
    book = Book()
    valid_publisher = "HarperCollins"
    book.set_publisher(valid_publisher)
    assert book.get_publisher() == valid_publisher

def test_invalid_publisher():
    # Test invalid publisher input
    book = Book()
    invalid_publisher = ""  # Empty string
    with pytest.raises(ValueError):
        book.set_publisher(invalid_publisher)
        
    invalid_publisher = 1  # Not a string
    with pytest.raises(ValueError):
        book.set_publisher(invalid_publisher)
        
    invalid_publisher = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla nec velit nec leo mattis fermentum eget ut magna. Sed tincidunt justo ut ultricies feugiat"  # String bigger than 100 characters
    with pytest.raises(ValueError):
        book.set_publisher(invalid_publisher)
    
    invalid_publisher = " HarperCollins " # Leading and trailing spaces
    with pytest.raises(ValueError):
        book.set_publisher(invalid_publisher)
        
    invalid_publisher = "1HarperCollins1" # Does not start or end with alphabetic characters
    with pytest.raises(ValueError):
        book.set_publisher(invalid_publisher)
    
    invalid_publisher = "!HarperCollins," # Does not start or end with alphabetic characters
    with pytest.raises(ValueError):
        book.set_publisher(invalid_publisher)
        
def test_valid_genre():
    # Test valid genre input
    book = Book()
    valid_genre = "Educational"
    book.set_genre(valid_genre)
    assert book.get_genre() == valid_genre

def test_invalid_genre():
    # Test invalid genre input
    book = Book()
    invalid_genre = ""  # Empty string
    with pytest.raises(ValueError):
        book.set_genre(invalid_genre)
        
    invalid_genre = 1  # Not a string
    with pytest.raises(ValueError):
        book.set_genre(invalid_genre)
        
    invalid_genre = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla nec velit nec leo mattis fermentum eget ut magna. Sed tincidunt justo ut ultricies feugiat"  # String bigger than 100 characters
    with pytest.raises(ValueError):
        book.set_genre(invalid_genre)
    
    invalid_genre = " Educational " # Leading and trailing spaces
    with pytest.raises(ValueError):
        book.set_genre(invalid_genre)
        
    invalid_genre = "1Educational1" # Does not start or end with alphabetic characters
    with pytest.raises(ValueError):
        book.set_genre(invalid_genre)
    
    invalid_genre = "!Educational," # Does not start or end with alphabetic characters
    with pytest.raises(ValueError):
        book.set_genre(invalid_genre)
           
def test_valid_edition():
    # Test valid edition input
    book = Book()
    valid_edition = 1
    book.set_edition(valid_edition)
    assert book.get_edition() == valid_edition     

def test_invalid_edition():
    # Test invalid edition input
    book = Book()
    invalid_edition = ""  # Empty string
    with pytest.raises(ValueError):
        book.set_edition(invalid_edition)
        
    invalid_edition = "foo"  # String
    with pytest.raises(ValueError):
        book.set_edition(invalid_edition)
    
    invalid_edition = 5.0  # Float
    with pytest.raises(ValueError):
        book.set_edition(invalid_edition)
        
    invalid_edition = 0  # Zero integer
    with pytest.raises(ValueError):
        book.set_edition(invalid_edition)
        
    invalid_edition = -1  # Negative integer
    with pytest.raises(ValueError):
        book.set_edition(invalid_edition)
        
def test_valid_publication_date():
    # Test valid publication date input
    book = Book()
    valid_publication_date = "25-02-2024"
    book.set_publication_date(valid_publication_date)
    assert book.get_publication_date() == valid_publication_date
    
def test_invalid_publication_date():
    # Test invalid publication date input
    book = Book()
    invalid_publication_date = ""  # Empty string
    with pytest.raises(ValueError):
        book.set_publication_date(invalid_publication_date)
        
    invalid_publication_date = 1  # Not a string
    with pytest.raises(ValueError):
        book.set_publication_date(invalid_publication_date)
        
    invalid_publication_date = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"  # String bigger than 10 characters
    with pytest.raises(ValueError):
        book.set_publication_date(invalid_publication_date)
    
    invalid_publication_date = "25-02-2024-2"  # String with more than 2 '-' characters
    with pytest.raises(ValueError):
        book.set_publication_date(invalid_publication_date)
        
    invalid_publication_date = "25-022024"  # String with less than 2 '-' characters
    with pytest.raises(ValueError):
        book.set_publication_date(invalid_publication_date)
        
    invalid_publication_date = " 25-02-2024 " # Leading and trailing spaces
    with pytest.raises(ValueError):
        book.set_publication_date(invalid_publication_date)
    
    invalid_publication_date = "!25-02-2024," # Does not start or end with alphabetic characters
    with pytest.raises(ValueError):
        book.set_publication_date(invalid_publication_date)
        
    invalid_publication_date = "foo-02-2024" # Set of non integer characters
    with pytest.raises(ValueError):
        book.set_publication_date(invalid_publication_date)
    
    invalid_publication_date = "25-foo-2024" # Set of non integer characters
    with pytest.raises(ValueError):
        book.set_publication_date(invalid_publication_date)
        
    invalid_publication_date = "25-02-foo" # Set of non integer characters
    with pytest.raises(ValueError):
        book.set_publication_date(invalid_publication_date)
    
    invalid_publication_date = "25.0-02-2024" # Set of non integer characters
    with pytest.raises(ValueError):
        book.set_publication_date(invalid_publication_date)
    
    invalid_publication_date = "25-02.0-2024" # Set of non integer characters
    with pytest.raises(ValueError):
        book.set_publication_date(invalid_publication_date)
        
    invalid_publication_date = "25-02-2024.0" # Set of non integer characters
    with pytest.raises(ValueError):
        book.set_publication_date(invalid_publication_date)
    
    invalid_publication_date = "50-02-2024" # Set of out of range dates
    with pytest.raises(ValueError):
        book.set_publication_date(invalid_publication_date)
    
    invalid_publication_date = "00-02-2024" # Set of out of range dates
    with pytest.raises(ValueError):
        book.set_publication_date(invalid_publication_date)
    
    invalid_publication_date = "25-25-2024" # Set of out of range dates
    with pytest.raises(ValueError):
        book.set_publication_date(invalid_publication_date)
        
    invalid_publication_date = "25-00-2024" # Set of out of range dates
    with pytest.raises(ValueError):
        book.set_publication_date(invalid_publication_date)
        
    invalid_publication_date = "25-02-3000" # Set of out of range dates
    with pytest.raises(ValueError):
        book.set_publication_date(invalid_publication_date)
    
    invalid_publication_date = "25-02-0000" # Set of out of range dates
    with pytest.raises(ValueError):
        book.set_publication_date(invalid_publication_date)
        
    invalid_publication_date = "25-02-1500" # Set of out of range dates
    with pytest.raises(ValueError):
        book.set_publication_date(invalid_publication_date)
    
def test_valid_description():
    # Test valid description input
    book = Book()
    valid_description = "Discover the essential principles and techniques of object-oriented programming in Python with this comprehensive guide, perfect for beginners and experienced programmers alike"
    book.set_description(valid_description)
    assert book.get_description() == valid_description 
    
def test_invalid_description():
    # Test invalid genre input
    book = Book()
    invalid_description = ""  # Empty string
    with pytest.raises(ValueError):
        book.set_description(invalid_description)
        
    invalid_description = 1  # Not a string
    with pytest.raises(ValueError):
        book.set_description(invalid_description)
        
    invalid_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla nec velit nec leo mattis fermentum eget ut magna. Sed tincidunt justo ut ultricies feugiat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla nec velit nec leo mattis fermentum eget ut magna. Sed tincidunt justo ut ultricies feugiat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla nec velit nec leo mattis fermentum eget ut magna. Sed tincidunt justo ut ultricies feugiat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla nec velit nec leo mattis fermentum eget ut magna. Sed tincidunt justo ut ultricies feugiat"  # String bigger than 500 characters
    with pytest.raises(ValueError):
        book.set_description(invalid_description)
    
    invalid_description = " Discover the essential principles and techniques of object-oriented programming in Python with this comprehensive guide, perfect for beginners and experienced programmers alike " # Leading and trailing spaces
    with pytest.raises(ValueError):
        book.set_description(invalid_description)
        
    invalid_description = "1Discover the essential principles and techniques of object-oriented programming in Python with this comprehensive guide, perfect for beginners and experienced programmers alike1" # Does not start or end with alphabetic characters
    with pytest.raises(ValueError):
        book.set_description(invalid_description)
    
    invalid_description = "!Discover the essential principles and techniques of object-oriented programming in Python with this comprehensive guide, perfect for beginners and experienced programmers alike," # Does not start or end with alphabetic characters
    with pytest.raises(ValueError):
        book.set_description(invalid_description)
    
def test_valid_price():
    # Test valid price input
    book = Book()
    valid_price = 9.99
    book.set_price(valid_price)
    assert book.get_price() == valid_price     

def test_invalid_price():
    # Test invalid price input
    book = Book()
    invalid_price = ""  # Empty string
    with pytest.raises(ValueError):
        book.set_price(invalid_price)
        
    invalid_price = "foo"  # String
    with pytest.raises(ValueError):
        book.set_price(invalid_price)
    
    invalid_price = 0  # Zero integer
    with pytest.raises(ValueError):
        book.set_price(invalid_price)
        
    invalid_price = -1  # Negative integer
    with pytest.raises(ValueError):
        book.set_price(invalid_price)
    
    invalid_price = 9  # Integer
    with pytest.raises(ValueError):
        book.set_price(invalid_price)
    
    invalid_price = 0.00  # Zero float
    with pytest.raises(ValueError):
        book.set_price(invalid_price)
         
    invalid_price = -1.00  # Negative float
    with pytest.raises(ValueError):
        book.set_price(invalid_price)
        
def test_valid_isbn():
    # Test valid ISBN input
    book = Book()
    valid_isbn = "123-4-56-789123-0"
    book.set_isbn(valid_isbn)
    assert book.get_isbn() == valid_isbn 
    
def test_invalid_isbn():
    # Test invalid publication date input
    book = Book()
    invalid_isbn = ""  # Empty string
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
        
    invalid_isbn = 1  # Not a string
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
        
    invalid_isbn = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"  # String bigger than 17 characters
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)

    invalid_isbn = "111-1-11-111111-1-1"  # String with more than 4 '-' characters
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
        
    invalid_isbn = "111-1-11-111111"  # String with less than 4 '-' characters
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
        
    invalid_isbn = " 111-1-11-111111-1 " # Leading and trailing spaces
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
    
    invalid_isbn = "!111-1-11-111111-1," # Does not start or end with alphabetic characters
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
        
    invalid_isbn = "foo-1-11-111111-1" # Set of non integer characters
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
    
    invalid_isbn = "111-foo-11-111111-1" # Set of non integer characters
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
        
    invalid_isbn = "111-1-foo-111111-1" # Set of non integer characters
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
        
    invalid_isbn = "111-1-11-foo-1" # Set of non integer characters
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
        
    invalid_isbn = "111-1-11-111111-foo" # Set of non integer characters
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
        
    invalid_isbn = "1.0-1-11-111111-1" # Set of non integer characters
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
    
    invalid_isbn = "111-1.0-11-111111-1" # Set of non integer characters
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
        
    invalid_isbn = "111-1-1.0-111111-1" # Set of non integer characters
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
        
    invalid_isbn = "111-1-11-1.0-1" # Set of non integer characters
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
        
    invalid_isbn = "111-1-11-111111-1.0" # Set of non integer characters
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
    
    invalid_isbn = "11-1-11-111111-1" # Set out of range sets
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
        
    invalid_isbn = "1111-1-11-111111-1" # Set out of range sets
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
        
    invalid_isbn = "11-11-11-111111-1" # Set out of range sets
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
        
    invalid_isbn = "11-1-1-111111-1" # Set out of range sets
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
        
    invalid_isbn = "11-1-111-111111-1" # Set out of range sets
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
        
    invalid_isbn = "11-1-11-11111-1" # Set out of range sets
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
    
    invalid_isbn = "11-1-11-1111111-1" # Set out of range sets
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
    
    invalid_isbn = "11-1-11-111111-11" # Set out of range sets
    with pytest.raises(ValueError):
        book.set_isbn(invalid_isbn)
           
def test_valid_quantity():
    # Test valid quantity input
    book = Book()
    valid_quantity = 1
    book.set_quantity(valid_quantity)
    assert book.get_quantity() == valid_quantity    
      
def test_invalid_quantity():
    # Test invalid quantity input
    book = Book()
    invalid_quantity = ""  # Empty string
    with pytest.raises(ValueError):
        book.set_quantity(invalid_quantity)
        
    invalid_quantity = "foo"  # String
    with pytest.raises(ValueError):
        book.set_quantity(invalid_quantity)
    
    invalid_quantity = 5.0  # Float 
    with pytest.raises(ValueError):
        book.set_quantity(invalid_quantity)
        
    invalid_quantity = -1  # Negative integer
    with pytest.raises(ValueError):
        book.set_quantity(invalid_quantity)
        
###################################################################################################
#################################       CLASSMETHOD TESTS       ###################################
###################################################################################################
def test_validate():
    # Test validation of book
    book = Book.authenticate_isbn(session, "111-2-33-444444-5")
    assert book is not None
    
    book = Book.authenticate_isbn(session, "999-8-77-666666-5")
    assert book is None
     
def test_register():
    # Test registration of book
    valid_book = {
        "title": "A Song of Ice and Fire: A Game of Thrones",
        "author": "George Martin",
        "publisher": "HarperCollins",
        "genre": "Fantasy",
        "edition": 1,
        "publication_date": "01-09-1996",
        "description": "A gripping tale of power struggles and intrigue set in a fantasy world where noble houses vie for control, while ancient forces awaken",
        "price": 29.99,
        "isbn": "978-0-00-747715-9"
    }
    
    # Assert if register() returns True -> Book sucessfully registered
    if Book.authenticate_isbn(session, valid_book["isbn"]) is None:
        assert Book.register(session, valid_book["title"], valid_book["author"], valid_book["publisher"], valid_book["genre"], valid_book["edition"], valid_book["publication_date"], valid_book["description"], valid_book["price"], valid_book["isbn"]) == True
        
    invalid_book = {
        "title": "OOP Python Fundamentals",
        "author": "Ricardo Silva",
        "publisher": "HarperCollins",
        "genre": "Educational",
        "edition": 1,
        "publication_date": "25-02-2024",
        "description": "Discover the essential principles and techniques of object-oriented programming in Python with this comprehensive guide, perfect for beginners and experienced programmers alike",
        "price": 9.99,
        "isbn": "111-2-33-444444-5"
    }
    
    # Assert if register() returns False -> Book failed to register
    if not Book.authenticate_isbn(session, invalid_book["isbn"]):
        assert Book.register(session, invalid_book["title"], invalid_book["author"], invalid_book["publisher"], invalid_book["genre"], invalid_book["edition"], invalid_book["publication_date"], invalid_book["description"], invalid_book["price"], invalid_book["isbn"]) == False
   
def test_add():
    # Existing ISBN and matching data from book in the database
    valid_book = {
        "title": "Harry Potter and The Philosopher's Stone",
        "author": "JK Rowling",
        "publisher": "Scholastic Corporation",
        "genre": "Fantasy",
        "edition": 1,
        "publication_date": "26-06-1997",
        "description": "Young wizard Harry discovers a hidden world of magic at Hogwarts School, facing dark forces",
        "price": 24.99,
        "isbn": "978-0-74-753269-6"
    }
    
    existing_book = Book.authenticate_isbn(session, valid_book["isbn"])
    
    if existing_book is not None:
        # Assert if add() returns True -> Sucessfully added book
        assert Book.add(session, existing_book) == True
    
    # Non existing ISBN from book in the database
    invalid_book = {
        "title": "Java Fundamentals",
        "author": "Ricardo Silva",
        "publisher": "HarperCollins",
        "genre": "Educational",
        "edition": 1,
        "publication_date": "15-10-2020",
        "description": "Discover the essential principles and techniques of Java programming with this comprehensive guide, perfect for beginners and experienced programmers alike",
        "price": 12.99,
        "isbn": "999-8-77-666666-5"
    }
    
    non_existing_book = Book.authenticate_isbn(session, invalid_book["isbn"])
    
    if non_existing_book is not None:
    # Assert if add() returns False -> Failed to add book
        assert Book.add(session, non_existing_book) == True
     
def test_authenticate_title():
    # Test authentication of book title
    books = Book.authenticate_title(session, "OOP Python Fundamentals")
    assert books is not None
    assert len(books) == 1
    
    books = Book.authenticate_title(session, "The Lord of the Rings")
    assert books is None
    
def test_authenticate_author():
    # Test authentication of book author
    books = Book.authenticate_author(session, "Ricardo Silva")
    assert books is not None
    assert len(books) == 1
    
    books = Book.authenticate_author(session, "JRR Tolkien")
    assert books is None
    
def test_authenticate_publisher():
    # Test authentication of book publisher
    books = Book.authenticate_publisher(session, "Scholastic Corporation")
    assert books is not None
    assert len(books) == 1
    
    books = Book.authenticate_publisher(session, "Pearson")
    assert books is None
    
def test_authenticate_genre():
    # Test authentication of book genre
    books = Book.authenticate_genre(session, "Fantasy")
    assert books is not None
    assert len(books) == 2
    
    books = Book.authenticate_genre(session, "Romance")
    assert books is None
    
def test_authenticate_edition():
    # Test authentication of book edition
    books = Book.authenticate_edition(session, 1)
    assert books is not None
    assert len(books) == 3
    
    books = Book.authenticate_edition(session, 9)
    assert books is None
    
def test_authenticate_publication_date():
    # Test authentication of book publication date
    books = Book.authenticate_publication_date(session, "25-02-2024")
    assert books is not None
    assert len(books) == 1
    
    books = Book.authenticate_publication_date(session, "01-01-1990")
    assert books is None
     
def test_authenticate_price():
    # Test authentication of book publication date
    books = Book.authenticate_price(session, 9.99)
    assert books is not None
    assert len(books) == 1
    
    books = Book.authenticate_price(session, 1.99)
    assert books is None