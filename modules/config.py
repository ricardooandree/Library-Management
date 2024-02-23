###################################################################################################
#######################################       IMPORTS       #######################################
###################################################################################################
import json
from modules.user import User

###################################################################################################
#####################################       FUNCTIONS        ######################################
###################################################################################################
def load_admin_accounts(session, file_path):
    """Loads the admin accounts from the json file"""
    
    # Opens configuration file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Gets the list of admin accounts
    admin_accounts = data.get("admins", [])
    
    for admin in admin_accounts:
        # Validates if the admin account doesn't exist
        if User.validate(session , admin['username'], admin['password'], admin['password']):
            # Register admin account
            User.register(session, admin['username'], admin['password'], admin=True)
