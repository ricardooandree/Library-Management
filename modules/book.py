###################################################################################################
#######################################       IMPORTS       #######################################
###################################################################################################
from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from modules.user import Base
from tabulate import tabulate

###################################################################################################
#######################################       CLASSES       #######################################
###################################################################################################
class Book(Base):
    __tablename__ = 'books'
    # Common attributes to each book object
    _id = Column(Integer, primary_key=True)
    _title = Column(String)
    _author = Column(String)
    _genre = Column(String)
    _publication_date = Column(String)
    _description = Column(String)
    _price = Column(Float)
    # Unique attributes to each book object
    _isbn = Column(String, unique=True)
    _availability = Column(Boolean)
    
    # Define setter methods for attributes
    def set_title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise ValueError("Title must be a string")
        
    def set_author(self, author):
        if isinstance(author, str):
            self._author = author
        else:
            raise ValueError("Author must be a string")
        
    def set_genre(self, genre):
        if isinstance(genre, str):
            self._genre = genre
        else:
            raise ValueError("Genre must be a string")
        
    def set_publication_date(self, publication_date):
        if isinstance(publication_date, str):
            self._publication_date = publication_date
        else:
            raise ValueError("Publication date must be a string")
    
    def set_description(self, description):
        if isinstance(description, str):
            self._description = description
        else:
            raise ValueError("Description must be a string")
    
    def set_price(self, price):
        if isinstance(price, float):
            self._price = price
        else:
            raise ValueError("Price must be a float")
        
    # FIXME: Add extra validation for isbn field needs to be a string like: '123-4-56-789123-0'
    def set_isbn(self, isbn):
        if isinstance(isbn, str):
            self._isbn = isbn
        else:
            raise ValueError("ISBN must be a string")
    
    def set_availability(self, availability):
        if isinstance(availability, bool):
            self._availability = availability
        else:
            raise ValueError("Availability must be a boolean")
        
    # Define getter methods for attributes
    def get_title(self):
        return self._title
    
    def get_author(self):
        return self._author
    
    def get_genre(self):
        return self._genre
    
    def get_publication_date(self):
        return self._publication_date
    
    def get_description(self):
        return self._description
    
    def get_price(self):
        return self._price
    
    def display_metadata(self):
        """Displays book metadata
        
        Args:
            No arguments are required.
            
        Returns:
            No return value.
            
        This instance method prints the book metadata as a string, this being, title, author, genre, publication date, and price.
        """
        print(f"Title: {self.get_title()}")
        print(f"Author: {self.get_author()}")
        print(f"Genre: {self.get_genre()}")
        print(f"Publication Date: {self.get_publication_date()}")
        print(f"Description: {self.get_description()}")
        print(f"Price: {self.get_price()}")
        
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
        """Validates book title
        
        Args: 
            session (Session): The SQLAlchemy session object to perform database queries.
            title (str): The title provided for authentication.
        
        Returns:
            book: If title exists in the database.
            None: If title does not exist in the database.
            
        This method checks if there's a book with a specific title.
        
        """
        # Query the database to find a book with the specified title
        book = session.query(Book).filter(Book._title == title).first()
        
        # Check if book exists in the database
        if book:
            return book
        else:
            return None
    
    @classmethod
    def authenticate_author(cls, session, author):
        """Validates book author
        
        Args: 
            session (Session): The SQLAlchemy session object to perform database queries.
            author (str): The author provided for authentication.
        
        Returns:
            book: If author exists in the database.
            None: If author does not exist in the database.
            
        This method checks if there's a book with a specific author.
        
        """
        # Query the database to find a book with the specified author
        book = session.query(Book).filter(Book._author == author).first()
        
        # Check if book exists in the database
        if book:
            return book
        else:
            return None
        
    @classmethod
    def register(cls, session, title, author, genre, publication_date, description, price, isbn):
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
        """
        # Create a new book object
        new_book = Book()
        
        # Check if new book was created successfully
        if new_book:
            # Set new book attributes
            new_book.set_title(title)
            new_book.set_author(author)
            new_book.set_genre(genre)
            new_book.set_publication_date(publication_date)
            new_book.set_description(description)
            new_book.set_price(price)
            new_book.set_isbn(isbn)
            new_book.set_availability(True)
            
            # Add the new book to the database
            session.add(new_book)
            
            # Commit the changes to the database
            session.commit()

            # Return new book object
            return new_book
        else:
            return None
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def rent_book(self, user):
        ...
    
    def return_book(self, user):
        ...
    
    def calculate_fine(self, user):
        ...
    