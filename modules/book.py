###################################################################################################
#######################################       IMPORTS       #######################################
###################################################################################################
from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from modules.user import Base

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
    
    # Getter methods
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
     
    # Setter methods NOTE: Create as needed only
    
    @classmethod
    def display_metadata(cls):
        """Displays book metadata"""
        print(f"Title: {cls.get_title()}")
        print(f"Author: {cls.get_author()}")
        print(f"Genre: {cls.get_genre()}")
        print(f"Publication Date: {cls.get_publication_date()}")
        print(f"Description: {cls.get_description()}")
        print(f"Price: {cls.get_price()}")
        
    @classmethod
    def authenticate_title(cls, session, title):
        """Authenticates book title"""
        # Query the database to find a book with the specified title
        book = session.query(Book).filter(Book._title == title).first()
        
        # Check if book exists in the database
        if book:
            return book
        else:
            return None
    
    @staticmethod
    def validate(session, isbn):
        """Validates book - isbn (unique for each book)"""
        # Query the database to find a book with the specified isbn
        book = session.query(Book).filter(Book._isbn == isbn).first()
        
        # Check if book exists in the database
        if not book:
            return True
        else:
            return False
    
    @classmethod
    def register(cls, session, title, author, genre, publication_date, description, price, isbn):
        """Register a new book in the database"""
        # Create a new book object
        new_book = Book()
        
        # Check if new book was created successfully
        if new_book:
            # Set new book attributes
            new_book._title = title
            new_book._author = author
            new_book._genre = genre
            new_book._publication_date = publication_date
            new_book._description = description
            new_book._price = price
            new_book._isbn = isbn
            new_book._availability = True
            
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
    