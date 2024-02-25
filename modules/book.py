###################################################################################################
#######################################       IMPORTS       #######################################
###################################################################################################
import re
from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from modules.user import Base
from tabulate import tabulate

###################################################################################################
#######################################       HELPERS       #######################################
###################################################################################################
headers = ["Title", "Author", "Publisher", "Genre", "Edition", "Publication Date", "Description", "Price", "ISBN"]

# Helper function for string attributes validation
def basic_string_attribute_validation(string, attribute):
    if isinstance(string, str):
        if not string[0].isalpha() or not string[-1].isalpha():
            return f"{attribute} must not start or end with non-alphabetical characters"
        
        elif len(string) > 100:
            return f"{attribute} must have a maximum of 100 characters"      
        else:
            return True
    else:
        return f"{attribute} must be an string"
        
###################################################################################################
#######################################       CLASSES       #######################################
###################################################################################################
class BookMismatchError(Exception):
    """Exception raised when provided book data does not match existing book"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
        
class Book(Base):
    __tablename__ = 'books'
    # Common attributes to each book object
    _id = Column(Integer, primary_key=True)
    _title = Column(String)
    _author = Column(String)
    _publisher = Column(String)
    _genre = Column(String)
    _edition = Column(Integer)
    _publication_date = Column(String)
    _description = Column(String)
    _price = Column(Float)
    # Unique attributes to each book object
    _isbn = Column(String, unique=True)
    _quantity = Column(Integer)
            
    # Define setter methods for attributes
    def set_title(self, title):
        # Call auxiliar function to validate basic string attribute features
        validation_result = basic_string_attribute_validation(title, attribute='Title')
        
        if isinstance(validation_result, str):
            raise ValueError(validation_result)

        # Set title attribute
        self._title = title
        
    def set_author(self, author):
        # Call auxiliar function to validate basic string attribute features
        validation_result = basic_string_attribute_validation(author, attribute='Author')
        
        if isinstance(validation_result, str):
            raise ValueError(validation_result)
    
        # Pattern FirstName LastName for author attribute and validation
        pattern = r'^[a-zA-Z]+\s[a-zA-Z]+$'
        if not re.match(pattern, author):
            raise ValueError("Author string should be of pattern: FirstName LastName with alphabetic characters only")
        
        # Set author attribute
        self._author = author

    def set_publisher(self, publisher):
        # Call auxiliar function to validate basic string attribute features
        validation_result = basic_string_attribute_validation(publisher, attribute='Publisher')
        
        if isinstance(validation_result, str):
            raise ValueError(validation_result)
        
        # Set publisher attribute
        self._publisher = publisher

    def set_genre(self, genre):
        # Call auxiliar function to validate basic string attribute features
        validation_result = basic_string_attribute_validation(genre, attribute='Genre')
        
        if isinstance(validation_result, str):
            raise ValueError(validation_result)

        # Set genre attribute
        self._genre = genre
    
    def set_edition(self, edition):
        # Edition attribute validation
        if not isinstance(edition, int):
            raise ValueError("Edition must be an integer")
        
        if edition <= 0:
            raise ValueError("Edition must be a positive integer")
        
        # Set edition attribute
        self._edition = edition
        
    def set_publication_date(self, publication_date):
        # Publication date attribute validation
        if not isinstance(publication_date, str):
            raise ValueError("Publication date must be a string")

        try:
            day, month, year = map(int, publication_date.split('-'))

        except ValueError:
            raise ValueError("Publication date must be of format dd-mm-yyyy")
        
        if not 1 <= day <= 31:
            raise ValueError("Publication date day must be in between 1 and 31")
        
        if not 1 <= month <= 12:
            raise ValueError("Publication date month must be in between 1 and 12")
            
        if not 1800 <= year <= 2100:
            raise ValueError("Publication date year must be in between 1800 and 2100")
        
        # Set publication date attribute
        self._publication_date = publication_date

    def set_description(self, description):
        # Description attribute validation
        if not isinstance(description, str):
            raise ValueError("Description must be a string")

        if len(description) > 500:
            raise ValueError("Description must have a maximum of 500 characters")

        if not description[0].isalpha() or not description[-1].isalpha():
            raise ValueError("Description must not start or end with non-alphabetical characters")

        # Set the description
        self._description = description

    def set_price(self, price):
        # Price attribute validation
        if not isinstance(price, float):
            raise ValueError("Price must be a float")
        
        if price <= 0:
            raise ValueError("Price must be a positive float")
        
        # Set price attribute
        self._price = price

    def set_isbn(self, isbn):
        # ISBN attribute validation
        if not isinstance(isbn, str):
            raise ValueError("ISBN must be a string")
        
        try:
            group1, group2, group3, group4, group5 = isbn.split('-')
        
        except ValueError:
            raise ValueError("ISBN must be of format 123-4-56-789012-3")
        
        if not group1.isdigit() or not len(group1) == 3:
            raise ValueError("ISBN first set must be a number and have 3 digits")
        
        if not group2.isdigit() or not len(group2) == 1:
            raise ValueError("ISBN second set must be a number and have 1 digit")
        
        if not group3.isdigit() or not len(group3) == 2:
            raise ValueError("ISBN third set must be a number and have 2 digits")
        
        if not group4.isdigit() or not len(group4) == 6:
            raise ValueError("ISBN fourth set must be a number and have 6 digits")
        
        if not group5.isdigit() or not len(group5) == 1:
            raise ValueError("ISBN fifth set must be a number and have 1 digit")
        
        # Set ISBN attribute
        self._isbn = isbn
            
    def set_quantity(self, quantity):
        # Quantity attribute validation
        if not isinstance(quantity, int):
            raise ValueError("Quantity must be a boolean")
        
        # Set quantity attribute
        self._quantity = quantity
        
    # Define getter methods for attributes
    def get_title(self):
        return self._title
    
    def get_author(self):
        return self._author
    
    def get_publisher(self):
        return self._publisher
    
    def get_genre(self):
        return self._genre
    
    def get_edition(self):
        return self._edition
    
    def get_publication_date(self):
        return self._publication_date
    
    def get_description(self):
        return self._description
    
    def get_price(self):
        return self._price
    
    def get_isbn(self):
        return self._isbn
    
    def get_quantity(self):
        return self._quantity
    
    def display_metadata(books):
        """Displays book metadata
        
        Args:
            No arguments are required.
            
        Returns:
            No return value.
            
        This instance method prints the book metadata as a string, this being, title, author, genre, publication date, and price.
        """
        table = []
        for book in books:
            row = [book.get_title(), book.get_author(), book.get_publisher(), book.get_genre(), book.get_edition(), book.get_publication_date(), book.get_description(), book.get_price(), book.get_isbn()]
            table.append(row)
        
        print(tabulate(table, headers, tablefmt="double_outline"))
        
    @classmethod
    def validate(cls, session, isbn):
        """Validates book existence
        
        Args:
            session (Session): The SQLAlchemy session object to perform database queries.
            isbn (str): the isbn provided to validate the book.
            
        Returns:
            bool: True if the book does not exist in the database, False otherwise.
            
        This method checks if there's a book in the database with the specified isbn since isbn is unique for each book, which means, checking if the book exists in the database or not.
        """
        # Query the database to find a book with the specified isbn
        book = session.query(Book).filter(Book._isbn == isbn).first()
        
        # Check if book with specific isbn exists in the database
        if not book:
            return True
        else:
            return False
        
    @classmethod
    def authenticate_title(cls, session, title):
        """Authenticates book title
        
        Args: 
            session (Session): The SQLAlchemy session object to perform database queries.
            title (str): The title provided for authentication.
        
        Returns:
            book (list): If book with specific title exists in the database.
            None: If title does not exist in the database.
            
        This method checks if there's any books with a specific title in the database and filters them by uniqueness.
        
        """
        # Query to get all books with the given title and distinct isbn
        books = session.query(Book).filter(Book._title == title).distinct(Book._isbn).all()
        
        # Check if there's any book with the given title in the database
        if books:
            return books
        else:
            return None
    
    @classmethod
    def authenticate_author(cls, session, author):
        """Authenticates book author
        
        Args: 
            session (Session): The SQLAlchemy session object to perform database queries.
            author (str): The author provided for authentication.
        
        Returns:
            book (list): If book with specific author exists in the database.
            None: If author does not exist in the database.
            
        This method checks if there's any books with a specific author in the database and filters them by uniqueness.
        
        """
        # Query to get all books with the given author and distinct isbn
        books = session.query(Book).filter(Book._author == author).distinct(Book._isbn).all()
        
        # Check if book exists in the database
        if books:
            return books
        else:
            return None
    
    @classmethod
    def authenticate_publisher(cls, session, publisher):
        """Authenticates book publisher
        
        Args: 
            session (Session): The SQLAlchemy session object to perform database queries.
            publisher (str): The publisher provided for authentication.
        
        Returns:
            book (list): If book with specific publisher exists in the database.
            None: If publisher does not exist in the database.
            
        This method checks if there's any books with a specific publisher in the database and filters them by uniqueness.
        
        """
        # Query to get all books with the given publisher and distinct isbn
        books = session.query(Book).filter(Book._publisher == publisher).distinct(Book._isbn).all()
        
        # Check if book exists in the database
        if books:
            return books
        else:
            return None
    
    @classmethod
    def authenticate_genre(cls, session, genre):
        """Authenticates book genre
        
        Args: 
            session (Session): The SQLAlchemy session object to perform database queries.
            genre (str): The genre provided for authentication.
        
        Returns:
            book (list): If book with specific genre exists in the database.
            None: If genre does not exist in the database.
            
        This method checks if there's any books with a specific genre in the database and filters them by uniqueness.
        
        """
        # Query to get all books with the given genre and distinct isbn
        books = session.query(Book).filter(Book._genre == genre).distinct(Book._isbn).all()
        
        # Check if book exists in the database
        if books:
            return books
        else:
            return None
    
    @classmethod
    def authenticate_edition(cls, session, edition):
        """Authenticates book edition
        
        Args: 
            session (Session): The SQLAlchemy session object to perform database queries.
            edition (int): The edition provided for authentication.
        
        Returns:
            book (list): If book with specific edition exists in the database.
            None: If edition does not exist in the database.
            
        This method checks if there's any books with a specific edition in the database and filters them by uniqueness.
        
        """
        # Query to get all books with the given edition and distinct isbn
        books = session.query(Book).filter(Book._edition == edition).distinct(Book._isbn).all()
        
        # Check if book exists in the database
        if books:
            return books
        else:
            return None
    
    @classmethod
    def authenticate_publication_date(cls, session, publication_date):
        """Authenticates book publication date
        
        Args: 
            session (Session): The SQLAlchemy session object to perform database queries.
            publication_date (str): The publication date provided for authentication.
        
        Returns:
            book (list): If book with specific publication date exists in the database.
            None: If publication date does not exist in the database.
            
        This method checks if there's any books with a specific publication date in the database and filters them by uniqueness.
        
        """
        # Query to get all books with the given publication date and distinct isbn
        books = session.query(Book).filter(Book._publication_date == publication_date).distinct(Book._isbn).all()
        
        # Check if book exists in the database
        if books:
            return books
        else:
            return None
    
    @classmethod
    def authenticate_price(cls, session, price):
        """Authenticates book price
        
        Args: 
            session (Session): The SQLAlchemy session object to perform database queries.
            price (float): The price provided for authentication.
        
        Returns:
            book (list): If book with specific price exists in the database.
            None: If price does not exist in the database.
            
        This method checks if there's any books with a specific price in the database and filters them by uniqueness.
        
        """
        # Query to get all books with the given price and distinct isbn
        books = session.query(Book).filter(Book._price == price).distinct(Book._isbn).all()
        
        # Check if book exists in the database
        if books:
            return books
        else:
            return None
    
    @classmethod
    def register(cls, session, title, author, publisher, genre, edition, publication_date, description, price, isbn):
        """Register a new book in the database
        
        Args:
            session (Session): The SQLAlchemy session object to perform database queries.
            title (str): The title provided for registration.
            author (str): The author provided for registration.
            genre (str): The genre provided for registration.
            publication_date (str): The publication date provided for registration.
            description (str): The description provided for registration.
            price (float): The price provided for registration.
            isbn (str): The isbn provided for registration.
        
        Returns: 
            book: If successfully registered a new book.
            None: If failed to register a new book. 
            
        This method created a new book object, sets its attributes and adds it to the database.
        """
        # Create a new book object
        new_book = Book()
        
        # Check if new book was created successfully
        if new_book:
            # Set new book attributes
            new_book.set_title(title)
            new_book.set_author(author)
            new_book.set_publisher(publisher)
            new_book.set_genre(genre)
            new_book.set_edition(edition)
            new_book.set_publication_date(publication_date)
            new_book.set_description(description)
            new_book.set_price(price)
            new_book.set_isbn(isbn)
            new_book.set_quantity(1)
            
            # Add the new book to the database
            session.add(new_book)
            
            # Commit the changes to the database
            session.commit()

            return True    # Successfully registered a new book
        else:
            return False    # Failed to register a new book
        
    @classmethod
    def add(cls, session, title, author, publisher, genre, edition, publication_date, description, price, isbn):
        """Add a new book to the database
        
        Args:
            session (Session): The SQLAlchemy session object to perform database queries.
            title (str): The title provided to validate the book to be added to the database.
            author (str): The author provided to validate the book to be added to the database.
            publisher (str): The publisher provided to validate the book to be added to the database.
            genre (str): The genre provided to validate the book to be added to the database.
            edition (int): The edition provided to validate the book to be added to the database.
            publication_date (string): The publication_date provided to validate the book to be added to the database.
            description (str): The description provided to validate the book to be added to the database.
            price (float): The price provided to vlaidate the book to be added to the database.
            isbn (str): The isbn provided to search for the book.
            
        Returns: 
            bool: True if successfully added a new book, false otherwise.
            
        This method alters the quantity of the book correspondent to the specified isbn to +1 in order to signify that the book was added to the database.
        """
        # Query the database to find a book with the specified isbn
        book = session.query(Book).filter(Book._isbn == isbn).first()
        
        # Check if book exists in the database
        if book:
            # Check if provided book data matches existing book
            attributes = {
                'title': title,
                'author': author,
                'publisher': publisher,
                'genre': genre,
                'edition': edition,
                'publication_date': publication_date,
                'description': description,
                'price': price
            }
            
            for attr, value in attributes.items():
                if getattr(book, f"get_{attr}")() != value:
                    raise BookMismatchError(f"Provided {attr} does not match existing book with ISBN: {isbn}")
            
            # Update the quantity of the book
            book.set_quantity(book.get_quantity() + 1)
            
            # Commit the changes to the database
            session.commit()

            return True    # Successfully added a new book
        else:
            return False   # Failed to add a new book
        

        
        
        
        
        
        
        
    def rent_book(self, user):
        ...
    
    def return_book(self, user):
        ...
    
    def calculate_fine(self, user):
        ...
    