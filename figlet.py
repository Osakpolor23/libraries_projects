# import the necessary libraries
import pyfiglet
import random
import sys



# initialize the Figlet engine 
figlet = pyfiglet.Figlet()

# get a list of all Figlet fonts
figlet_list = figlet.getFonts()

# define the main function()
def main():
    # validate arguments
    validate_commands()

    # get user inputs
    user_input = input("Input: ")

    # get the font
    font = get_font()

    # render and display output
    figlet.setFont(font=font) # set the font
    print(f"Output: \n{figlet.renderText(user_input)}") # \n to display on the next line


# define the validate commands function
def validate_commands():
    # ensure the arguments on the command-line is either 0 or 2 i.e file name aside
    if len(sys.argv) == 1: 
        return
    elif len(sys.argv) == 3:
        # check the arguments provided if they meet the conditions
        if sys.argv[1] not in("-f", "-font") or sys.argv[2] not in figlet_list:
            sys.exit("Invalid usage: Use '-f' or '--font' followed by a valid font name.")
    # if the arguments are neither 0 or 2
    else:
        # exit with the error message
        sys.exit("Invalid usage: Provide 0 or 2 arguments only.")

# define the get_font() function
def get_font():
    try:
        # if no argument provided i.e just the file name
        if len(sys.argv) == 1:
           # returm any random font
           return random.choice(figlet_list)
        # if the two arguments meet the requirements
        elif len(sys.argv) == 3:
            # return the font name provided in the command line
            return sys.argv[2]
    # if the provided font doesn't exist
    except pyfiglet.FontNotFound:
        # exit the program with the error message
        sys.exit("Font not found")
    
# call the main function when the file is executed directly
if __name__ == "__main__":
    main()

