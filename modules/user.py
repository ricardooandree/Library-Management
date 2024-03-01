###################################################################################################
#######################################       IMPORTS       #######################################
###################################################################################################
import re

from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash, generate_password_hash
from tabulate import tabulate

# Configuration
Base = declarative_base()

# Headers for table printing
headers = ["Username", "Total fee"]

# Helper function for string attributes validation
def basic_string_attribute_validation(string, attribute):
    # Basic string attribute validation
    if not isinstance(string, str):
        return f"{attribute} must be a string"
    
    if not string:
        return f"{attribute} cannot be empty"
    
    if len(string) > 50:
        return f"{attribute} must have a maximum of 50 characters"
    
    # Valid string
    return True
###################################################################################################
#######################################       CLASSES       #######################################
###################################################################################################
class User(Base):
    __tablename__ = 'users'
    _id = Column(Integer, primary_key=True)
    _username = Column(String, unique=True)
    _password = Column(String)
    _is_admin = Column(Boolean, default=False)
    _total_fee = Column(Float, default=0.0)
    
    # Define relationship with transactions
    transactions = relationship("Transaction", back_populates="user")
    
    # Define setter methods for attributes
    def set_username(self, username):
        # Call auxiliar function to validate basic string attribute features
        validation_result = basic_string_attribute_validation(username, attribute='Username')
        if isinstance(validation_result, str):
            raise ValueError(validation_result)
        
        # Regular expression pattern allowing alphanumeric characters and specified special characters
        pattern = r'^[a-zA-Z0-9_-]+$'

        # Match the input string against the pattern
        if not re.match(pattern, username):
            raise ValueError("Username can't contain spaces or special characters that are not - or _")
        
        # Set username attribute
        self._username = username
    
    def set_password(self, password):
        # Call auxiliar function to validate basic string attribute features
        validation_result = basic_string_attribute_validation(password, attribute='Password')
        if isinstance(validation_result, str):
            raise ValueError(validation_result)
        
        if ' ' in password:
            raise ValueError("Password cannot contain spaces")
        
        # Set password attribute
        self._password = generate_password_hash(password)
    
    def set_is_admin(self, is_admin):
        # is admin attribute validation
        if not isinstance(is_admin, bool):
            raise ValueError("is_admin must be a boolean")
        
        # Set is_admin attribute
        self._is_admin = is_admin
    
    def set_total_fee(self, fee):
        # Total fee attribute validation
        if not isinstance(fee, float):
            raise ValueError("Total fee must be a float")
        
        if fee < 0:
            raise ValueError("Total fee must be a positive float")
        
        # Set total fee attribute
        self._total_fee = fee
        
    # Define getter methods for attributes
    def get_id(self):
        return self._id
    
    def get_username(self):
        return self._username
    
    def get_password(self):
        return self._password
    
    def get_is_admin(self):
        return self._is_admin
    
    def get_total_fee(self):
        return self._total_fee
    
    def display(users):
        """Display users
        
        Args:
            user: User object that can be a list of objects or a single object to be displayed. 
            
        Returns:
            No return value.
            
        This instance method prints the users data such as their username and total fee amount.
        """
        table = []
        for user in users:
            row = [user.get_username(), user.get_total_fee()]
            table.append(row)
        
        print(tabulate(table, headers, tablefmt="double_outline"))
        
    @classmethod
    def validate(cls, session, username, password, confirm_password):
        """Validates user registration credentials
        
        Args:
            session (Session): The SQLAlchemy session object to perform database queries.
            username (str): The username provided during registration.
            password (str): The password provided during registration.
            confirm_password (str): The password confirmation provided during registration.
        
        Returns:
            bool: True if the credentials are valid, False otherwise.
            
        This method checks if the username is available (not already taken) and if the password matches the password confirmation. Additionally, it checks for password complexity requirements.
        
        """
        # Query the database to find a user with the specified username
        user = session.query(User).filter(User._username == username).first()
        
        # Check if user was found with the specified username
        if user:
            return False    # Validation failed
        else:
            # Check if password input matches the password confirmation
            if password == confirm_password:
                # TODO: Check if password meets safety requirements
                return True    # Validation successful
            else:
                return False # Validation failed
        
    @classmethod
    def authenticate(cls, session, username, password):
        """Authenticates user login credentials
        
        Args:
            session (Session): The SQLAlchemy session object to perform database queries.
            username (str): The username provided for authentication.
            password (str): The password provided for authentication.
        
        Returns:
            user: If the credentials are valid
            None: If the credentials are invalid
            
        This method checks if the username exists in the database and if it does, checks if the password of that user matches the one in the database.
        
        """
        # Query the database to find the username
        user = session.query(User).filter(User._username == username).first()
        
        # Check if user was found with the specified username
        if user:
            # Check if the input password is correct
            if check_password_hash(user.get_password(), password):
                return user    # Authentication successful
        else:
            return None    # Authentication failed
    
    @classmethod
    def authenticate_id(cls, session, user_id):
        """Authenticates user existence
        
        Args:
            session (Session): The SQLAlchemy session object to perform database queries.
            user_id (int): the id provided to validate the user.
            
        Returns:
            user: If book with specific ISBN exists in the database.
            None: If publication date does not exist in the database.
            
        This method checks if there's a user in the database with the specified id since id is unique for each user, which means, checking if the user exists in the database or not.
        """
        # Query the database to find a book with the specified id
        user = session.query(User).filter(User._id == user_id).first()
        
        # Check if book with specific id exists in the database
        if user:
            return user
        else:
            return None
        
    @classmethod
    def authenticate_username(cls, session, username):
        """Authenticates user existence
        
        Args:
            session (Session): The SQLAlchemy session object to perform database queries.
            username (str): The username provided to validate the user.
            
        Returns:
            user: If book with specific ISBN exists in the database.
            None: If publication date does not exist in the database.
            
        This method checks if there's a user in the database with the specified username since username is unique for each user, which means, checking if the user exists in the database or not.
        """
        # Query the database to find a user with the specified username
        user = session.query(User).filter(User._username == username).first()
        
        # Check if user was found with the specified username
        if user:
            return user
        else:
            return None
    
    @classmethod
    def register(cls, session, username, password, admin=False):
        """Register new user
        
        Args: 
            session (Session): The SQLAlchemy session object to perform database queries.
            username (str): The username provided during registration or configuration set up.
            password (str): The password provided during registration or configuration set up.
            admin (bool): Default set to False, True if admin is to be registrated.
        
        Returns:
            user: If successfully registered a new user.
            None: If registration failed.
            
        This method creates a new user with the given credentials and adds it to the database.
        
        """
        # Create a new User object
        new_user = User()
        
        # Check if new_user was created successfully
        if new_user:
            # Set new user credentials
            new_user.set_username(username)
            new_user.set_password(password)    # Password is hashed in set_password
            
            # Check if new_user is admin
            if admin:
                new_user.set_is_admin(True)
            
            # Add the new user to the session and commit to the database
            session.add(new_user)
            session.commit()
        
            # Return the newly created user object
            return new_user  
        else:
            return False    # Registration failed

    @classmethod
    def remove(cls, session, user):
        """Remove a user from the database
        
        Args:
            session (Session): The SQLAlchemy session object to perform database queries.
            user (User): The user to be removed from the database.
        
        Returns:
            bool: True if successfully removed a user from the database.
        
        This method removes a specified user from the database.
        """
        # Remove the book from the database
        session.delete(user)
        
        # Commit the changes to the database
        session.commit()
        
        return True    # Successfully removed a book
      
    @classmethod
    def get_all_fee(cls, session):
        """Get all users fees in the database
        
        Args:
            session (Session): The SQLAlchemy session object to perform database queries.
            
        Returns:
            books (list): A list of all users fees in the database.
            
        This method queries the database to get all the users fees in the database.
        """
        # Query the database to get all the books
        users = session.query(User).filter(User._total_fee > 0).all()
        
        # Check if book exists in the database
        if users:
            return users
        else:
            return None
        
    def rent_book(self, session, fee):
        """Rents a book
        """
        # Get user total fee
        total_fee = self.get_total_fee()
        
        # Sets the total fee amount
        self.set_total_fee(total_fee + fee)
        
        # Commit changes to the database
        session.commit()
        
        return True # Sucessfully rented a book
        
    def return_book(self, session, fee):
        """Return a book
        """
        # Get user total fee
        total_fee = self.get_total_fee()
        
        # Sets the total fee amount
        self.set_total_fee(total_fee - fee)
        
        # Commit changes to the database
        session.commit()
        
        return True # Sucessfully returned a book
    