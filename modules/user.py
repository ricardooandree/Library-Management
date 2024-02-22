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
    
    # TODO: Define relationships
    
    # Getter for is_admin
    #@property
    #def is_admin(self):
    #    return self._is_admin
    
    # Setter for is_admin
    #@is_admin.setter
    #def is_admin(self, value):
    #    if value in [True, False]:
    #        self._is_admin = value
    #    else:
    #        raise ValueError("is_admin must be True or False")
    
    @classmethod
    def validate(cls, session, username, password, confirm_password):
        # Query the database to find a user with the specified username
        user = session.query(User).filter(User.username == username).first()
        
        # Check if user was found with the specified username
        if not user:
            # Check if password input matches the password confirmation
            if password == confirm_password:
                # TODO: Check if password meets safety requirements
                return True    # Validation successful
            
        return False    # Validation failed
        
    @classmethod
    def authenticate(cls, session, username, password):
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
        # Create a new User object with credentials
        new_user = User(username=username, password=password)
        
        # Add the new user to the session and commit to the database
        session.add(new_user)
        session.commit()
        
        # Return the newly created user object
        return new_user  

    def get_books_rented(self):
        pass
    
    def pay_fine(self):
        pass
