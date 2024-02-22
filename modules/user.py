###################################################################################################
#######################################       IMPORTS       #######################################
###################################################################################################
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import check_password_hash, generate_password_hash

# Configuration
Base = declarative_base()

###################################################################################################
#######################################       CLASSES       #######################################
###################################################################################################
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    is_admin = Column(Boolean, default=False)
    # is_admin_column = Column(Boolean, default=False)
    
    # TODO: Define relationships
    
    # Getter for is_admin
    #@property
    #def is_admin(self):
    #    return self._is_admin
    
    # Setter for is_admin
    #@is_admin.setter
    #def is_admin(self, value):
    #    if isinstance(value, bool):
    #        self._is_admin = value
    #        self.is_admin_column = value  # Update the corresponding column in the database
    #    else:
    #        raise ValueError("is_admin must be True or False")
    
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
            
        This method checks if the username is available (not already taken) and if the password matches the password confirmation. Additionally, it checks for password complexity requirements in the future.
        
        """
        # Query the database to find a user with the specified username
        user = session.query(User).filter(User.username == username).first()
        
        # Check if no user was found with the specified username
        if not user:
            # Check if password input matches the password confirmation
            if password == confirm_password:
                # TODO: Check if password meets safety requirements
                return True    # Validation successful
            
        return False    # Validation failed
        
    @classmethod
    def authenticate(cls, session, username, password):
        """Authenticates user login credentials
        
        Args: 
            session (Session): The SQLAlchemy session object to perform database queries.
            username (str): The username provided during login.
            password (str): The password provided during login.
        
        Returns:
            user: If the credentials are valid
            None: If the credentials are invalid
            
        This method checks if the username exists in the database and if the password of that user matches the one in the database.
        
        """

        # Query the database to find the username
        user = session.query(User).filter(User.username == username).first()
        
        # Check if user was found with the specified username
        if user:
            # Check if the input password is correct
            if check_password_hash(user.password, password):
                return user    # Authentication successful
            
        return None    # Authentication failed
    
    @classmethod
    def register(cls, session, username, password):
        """Register new user
        
        Args: 
            session (Session): The SQLAlchemy session object to perform database queries.
            username (str): The username provided during registration.
            password (str): The password provided during registration.
        
        Returns:
            user: If successfully registered a new user.
            None: If registration failed.
            
        This method creates a new user with the given credentials and adds it to the database.
        
        """
        # Hash password
        hashed_password = generate_password_hash(password)
        
        # Create a new User object with credentials
        new_user = User(username=username, password=hashed_password)
        
        # Check if new_user was created successfully
        if new_user:
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
