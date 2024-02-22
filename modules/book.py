###################################################################################################
#######################################       IMPORTS       #######################################
###################################################################################################
from sqlalchemy import Column, Integer, String, ForeignKey, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Configuration
Base = declarative_base()

###################################################################################################
#######################################       CLASSES       #######################################
###################################################################################################
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    ISBN = Column(String)
    
    # TODO: Define relationships
    
    def rent_book(self, user):
        ...
    
    def return_book(self, user):
        ...
    
    def calculate_fine(self, user):
        ...
    