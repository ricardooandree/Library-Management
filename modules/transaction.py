###################################################################################################
#######################################       IMPORTS       #######################################
###################################################################################################
from sqlalchemy import Column, Float, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from modules.user import Base


###################################################################################################
#######################################       CLASSES       #######################################
###################################################################################################
class Transaction(Base):
    __tablename__ = 'transactions'
    _id = Column(Integer, primary_key=True)
    _user_id = Column(Integer, ForeignKey('users._id'))
    _book_id = Column(Integer, ForeignKey('books._id'))
    _type = Column(String)  # Type of transaction: rental or return
    _checkout_date = Column(Date)
    _return_date = Column(Date)
    _fee = Column(Float)
    
    # Define relationships
    user = relationship("User", back_populates="transactions")
    book = relationship("Book", back_populates="transactions")
    
    # FIXME: Add setters validation
    # Define setter methods for attributes
    def set_user_id(self, user_id):
        self._user_id = user_id
    
    def set_book_id(self, book_id):
        self._book_id = book_id
        
    def set_type(self, type):
        self._type = type
        
    def set_checkout_date(self, checkout_date):
        self._checkout_date = checkout_date
        
    def set_return_date(self, return_date):
        self._return_date = return_date
        
    def set_fee(self, fee):
        self._fee = fee
        
    # Define getter methods for attributes
    def get_type(self):
        return self._type
    
    def get_checkout_date(self):
        return self._checkout_date
    
    def get_return_date(self):
        return self._return_date
    
    def get_fee(self):
        return self._fee
    
    def display(self):
        ...

    @classmethod
    def register(cls, session, user_id, book_id, type, checkout_date, return_date, fee):
        """Register new transaction
        """
        # Create a new Transaction object
        new_transaction = Transaction()
        
        # Check if new_user was created successfully
        if new_transaction:
            # Set new transaction attributes
            new_transaction.set_user_id(user_id)
            new_transaction.set_book_id(book_id)
            new_transaction.set_type(type)
            new_transaction.set_checkout_date(checkout_date)
            new_transaction.set_return_date(return_date)
            new_transaction.set_fee(fee)
            
            # Add new transaction to the database
            session.add(new_transaction)
            session.commit()
            
            return True    # Registration successful
        else:
            return False    # Registration failed