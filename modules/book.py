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
headers = ["Title", "Author", "Publisher", "Genre", "Edition", "Publication Date", "Description", "Price", "ISBN"]

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
        if isinstance(title, str):
            self._title = title
        else:
            raise ValueError("Title must be a string")
        
    def set_author(self, author):
        if isinstance(author, str):
            self._author = author
        else:
            raise ValueError("Author must be a string")
    
    def set_publisher(self, publisher):
        if isinstance(publisher, str):
            self._publisher = publisher
        else:
            raise ValueError("Publisher must be a string")
        
    def set_genre(self, genre):
        if isinstance(genre, str):
            self._genre = genre
        else:
            raise ValueError("Genre must be a string")
    
    def set_edition(self, edition):
        if isinstance(edition, int):
            self._edition = edition
        else:
            raise ValueError("Edition must be an integer")
        
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
    
    def set_quantity(self, quantity):
        if isinstance(quantity, int):
            self._quantity = quantity
        else:
            raise ValueError("Quantity must be a boolean")
        
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
    def add(cls, session, isbn):
        """Add a new book to the database
        
        Args:
            session (Session): The SQLAlchemy session object to perform database queries.
             isbn (str): the isbn provided to search for the book.
        Returns: 
            bool: True if successfully added a new book, false otherwise.
            
        This method alters the quantity of the book correspondent to the specified isbn to +1 in order to signify that the book was added to the database.
        """
        # Query the database to find a book with the specified isbn
        book = session.query(Book).filter(Book._isbn == isbn).first()
        
        # Check if book exists in the database
        if book:
            # Update the quantity of the book
            book.set_quantity(book.get_quantity() + 1)
            
            # Commit the changes to the database
            session.commit()
            
            return True    # Sucessfully added a new book
        else:
            return False   # Failed to add a new book
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def rent_book(self, user):
        ...
    
    def return_book(self, user):
        ...
    
    def calculate_fine(self, user):
        ...
    