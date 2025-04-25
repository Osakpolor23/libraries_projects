# for this file, a virtual environment "adieu_env" was created to pip install inflect
# import package
import inflect # a package used to generate plurals, singular nouns, ordinals, indefinite articles,
               # and word-based representations of numbers.

# define the main function
def main():
    # get the names from the user
    song = get_name()
    # print the formatted "Adieu" message to the names
    print(song)


# define the get_name() function
def get_name():
    # call the inflect engine function()
    p = inflect.engine()
    # create an empty list to store the name inputs
    my_list = []
    # initialize an infinite loop
    while True:
        try:
            # prompt the user for Names
            name = input("Name: ")
            # append non-empty name inputs to the empty list
            if name.strip():
                my_list.append(name)
        # when the user inputs ctrl+D(i.e signals EOF),
        except EOFError:
            # return formatted "Adieu" message to the names, or an error message if no names were provided
            if not my_list:
                return "No names were provided. Goodbye!"
            return f"Adieu, adieu, to {p.join(my_list)}"  # the inflect library's join() method was used


# call the main function when the file is run directly on the command-prompt
if __name__ == "__main__":
    main()
    
