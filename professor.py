import random
import sys


# define the main function
def main():
    # get the level
    user_level = get_level()
    # create variables to track the loop number and score
    number = 0
    score = 0
    # create a loop that runs 10 times
    while number < 10:
        # generate two random integers
        X = generate_integer(user_level)
        Y = generate_integer(user_level)
        # carry out the addition
        expression = X + Y
        # create a loop that ensures the user is re-prompted on the same question
        # after each non-numeric input without skipping to the next
        while True:
            try:
                answer = int(input(f"{X} + {Y} = "))
                # only break out of this loop if numeric input is entered
                break
            except ValueError:
                print("EEE")
        # check if the answer provided is corrected
        if answer == expression:
            # increment the score if correct
            score += 1
        
        # if the answer is wrong, create an attempts loop that allows only 3 attempts
        else:
            attempts = 1 # ensure the first wrong attempt is counted before starting the loop
            # and print the error message -- this ensures that it is exactly 3 attemots
            # and not 4
            print("EEE")
            # initiate the loop
            while attempts < 3:
                try:
                    # get the user's input
                    answer = int(input(f"{X} + {Y} = "))
                    # check if the answer provided is correct
                    if answer == expression:
                        # if correct, increment the score and break out of the attempt loop
                        score += 1
                        break
                    # otherwise, print the error message
                    else:
                        print("EEE")
                # if a non-numeric input is entered, print an error message       
                except ValueError:
                    print("EEE")

                # increment the attempts everytime
                attempts += 1
            # only print the correct answer if and only if the attempts is 3,
            # and the answer is still not correct
            if attempts == 3 and answer != expression:
                print(f"{X} + {Y} = {expression}")

        # increment the number of the loop by 1 everytime a question is exhausted
        number += 1

    # finally, print the number of correct 
    print(f"Score: {score}")

# define the get_level() function
def get_level():
        # initiate an infinte loop that  asks for the level
        while True:
            try:
                level = int(input("Level: "))
                # check if level is between 1 and 3
                if 1 <= level <= 3:
                    # return level
                    return level # return also breaks the loop
            # catch the ValueError triggered by the int() function but silently ignore
            except ValueError:
                pass

# define the generate_integer() function
# which takes in the level from get_level() as a parameter
def generate_integer(level):
    # randomly geneterate integers that corresponds to the number of digits of the level
    # e.g level 1 will only geneterate single digits i.e between 0 and 9
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100, 999)
    # raise ValueError if the level from get_level() is not anything between 1 and 3
    else:
        raise ValueError
    


# call the main function only if the program is run directly in the command-line
if __name__ == "__main__":
    main()
