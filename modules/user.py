###################################################################################################
#######################################       IMPORTS       #######################################
###################################################################################################
from sqlalchemy import Column, Integer, String, ForeignKey, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Configuration
Base = declarative_base()

###################################################################################################
######################################       FUNCTIONS       ######################################
###################################################################################################
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    title = Column(String)  # Admin or User
    username = Column(String)
    password = Column(String)
    name = Column(String)
    email = Column(String)
    
    # TODO: Define relationships
    
    def get_books_rented(self):
        ...
    
    def pay_fine(self):
        ...