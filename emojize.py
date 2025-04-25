# for this project, I created a virtual environment know as emoji_env
# to install the project dependencies such as the emoji package
# import libraries
import sys
import emoji

# define the main function
def main():
    # get user input
    user_input = input("Input: ")
    # print the emojized version
    print(f"Output: {emojized(user_input)}")

# define the emojized function() to take in text as a parameter
def emojized(text):
    # return the emojize version of the text
    return emoji.emojize(text, language = 'alias') # it should also allow aliases



# call the main function if run directly on the command-line
if __name__ == "__main__":
    main()
