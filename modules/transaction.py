###################################################################################################
#######################################       IMPORTS       #######################################
###################################################################################################
from sqlalchemy import Column, Float, Integer, String, ForeignKey, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Configuration
Base = declarative_base()

###################################################################################################
#######################################       CLASSES       #######################################
###################################################################################################
class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    checkout_date = Column(Date)
    return_date = Column(Date)
    fine = Column(Float)
    
    # TODO: Define relationships
    
    def display(self):
        ...
