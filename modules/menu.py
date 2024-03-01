###################################################################################################
#######################################       IMPORTS       #######################################
###################################################################################################
from pyfiglet import Figlet

###################################################################################################
#######################################       CLASSES       #######################################
###################################################################################################
class Menu:
    def __init__(self, title, options):
        self.title = title
        self.options = options
    
    def display(self):
        """Display the menu"""
        # Create figlet object and set font
        figlet = Figlet()
        figlet.setFont(font="slant")
        
        # Print menu
        print(figlet.renderText(self.title))
        for index, option in enumerate(self.options, start=1):
            print(f"{index}- {option}")
        
        # Get user choice
        return input("\nEnter your choice: ")
