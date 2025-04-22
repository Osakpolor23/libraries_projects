# import libraries
import random
import sys


# define the main function
def main():
    # get the level
    user_level = get_level()
    # initiate an infinite loop
    while True:
        # generate integer and parse user_level as an argument
        number = generate_integer(user_level)
        # prompt the user to make a guess
        # initiate an infinite loop that only stop when a guess of a positive integer is made
        while True:
            try:
                # prompt the user for a guess
                guess = int(input("Guess: "))
                # check if the guess is a positive integer
                if guess > 0:
                    # if yes, break out of this loop
                    break
                # if the guess is not a positive integer
                else:
                    # continue the loop
                    continue
            # catch the ValueError that might arise from numeric inputs
            except ValueError:
                # silently ignore the error
                pass
        # check if guess is less than the generated number
        if guess < number:
            # print "Too small!" if it is
            print("Too small!")
        # check if the guess is greater than the generated number
        elif guess > number:
            # print "Too large!" if it is
            print("Too large!")
        # if the guess is correct
        else:
            # print "Just right!" and exit the program
            sys.exit("Just right!")
            

# define the get_level() function
def get_level():
        # initiate an infinte loop that  asks for the level
        while True:
            try:
                # prompt the user for the level which must be a numeric input
                level = int(input("Level: "))
                # check if level is a positive integer
                if level > 0:
                    # return level and break out of the loop if it is
                    return level
                # check if the input is not a positive integer
                else:
                    # continue the prompting for the level
                    continue
            # catch the ValueError that might arise from non-numeric inputs
            except ValueError:
                # silently ignore
                pass

# define generate_integer() function and parse level as a parameter
def generate_integer(level):
    # randomly generate integers between 1 and the selected level
    return random.randint(1, level)

# call the main function to execute only when the file is run directly
if __name__ == "__main__":
    main()