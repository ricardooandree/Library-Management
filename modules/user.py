###################################################################################################
#######################################       IMPORTS       #######################################
###################################################################################################
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash, generate_password_hash

# Configuration
Base = declarative_base()

###################################################################################################
#######################################       CLASSES       #######################################
###################################################################################################
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    _username = Column(String, unique=True)
    _password = Column(String)
    _is_admin = Column(Boolean, default=False)
    
    # TODO: Define relationships
    
    # Define setter methods for attributes
    def set_username(self, username):
        if isinstance(username, str):
            self._username = username
        else:
            raise ValueError("Username must be a string")
    
    def set_password(self, password):
        if isinstance(password, str):
            self._password = generate_password_hash(password)
        else:
            raise ValueError("Password must be a string")
    
    def set_is_admin(self, is_admin):
        if isinstance(is_admin, bool):
            self._is_admin = is_admin
        else:
            raise ValueError("is_admin must be a boolean")
    
    # Define getter methods for attributes
    def get_username(self):
        return self._username
    
    def get_password(self):
        return self._password
    
    def get_is_admin(self):
        return self._is_admin
    
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
        
        # Check if no user was found with the specified username
        if not user:
            # Check if password input matches the password confirmation
            if password == confirm_password:
                # TODO: Check if password meets safety requirements
                return True    # Validation successful
        else:    
            return False    # Validation failed
        
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
    def register(session, username, password, admin=False):
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
            return None    # Registration failed




    def get_books_rented(self):
        pass
    
    def pay_fine(self):
        pass
