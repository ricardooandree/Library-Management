###################################################################################################
#######################################       IMPORTS       #######################################
###################################################################################################
import sys
import os

# Add the parent directory (Library-Management) to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from modules.book import Book

###################################################################################################
####################################       SETTER TESTS       #####################################
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
        
    
    