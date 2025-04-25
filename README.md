# Python Libraries: Creative Projects

This repository contains a collection of Python programs that utilize various libraries to solve problems, enhance creativity, and foster interactive coding experiences. Each program is uniquely crafted to showcase the power of Python libraries in real-world scenarios. The projects are designed to be educational, fun, and engaging, making them suitable for learners and enthusiasts alike.

## Projects Overview
The projects in this repository are designed to demonstrate the capabilities of Python libraries in various domains, including data fetching, game development, text formatting, and emoji handling. Each project is self-contained and can be run independently.
The following projects are included in this repository:

### **1. bitcoin.py**

**Description**

bitcoin.py fetches the real-time market price of Bitcoin using the ***[CoinCap Bitcoin Price Index API] (https://pro.coincap.io/dashboard)***. It calculates the value of a user-specified number of bitcoins inputed on the command-line and handles invalid inputs gracefully.

**Features**

    Uses the requests library for API calls.

    Fetches real-time Bitcoin data.

    Handles API errors and non-numeric inputs seamlessly.

**Sample Input:**

    $ python bitcoin.py 2

**Expected Output:**

    $56,900.0000 (or the current price of 2 Bitcoin)

### **2. professor.py**

**Description**

professor.py is a math quiz game where players answer 10 randomly generated arithmetic problems. Players can choose their difficulty level, and the program provides detailed feedback for correct and incorrect answers. This is modeled after the 1970's ***[Little Professor] (https://www.youtube.com/watch?v=ZuJwzH9BIgs&embeds_referring_euri=https%3A%2F%2Fcs50.harvard.edu%2F&source_ve_path=Mjg2NjY)*** game, where a computer would ask random math questions and provide feedback.

**Features**

    Generates random math problems based on user-selected difficulty.

    Allows for three attempts for every incorrect answer and provides the answer after the third incorrect attempt.

    Tracks the number of correct answers and provides feedback.

    Displays the final score at the end.

    Handles invalid inputs gracefully.

**Sample Interaction:**

    Level: 1
    3 + 5 = 8
    7 + 9 = 15
    EEE
    7 + 9 = 12
    EEE
    7 + 9 = 14
    EEE
    7 + 9 = 16
    4 + 8 = 12
    ...
    Score: 4 ( based on other correct answers)

### **3. game.py**

**Description**

game.py is a guessing game where users attempt to guess a randomly generated number within a range determined by their chosen difficulty level.

**Features**

    Generates a random number based on the selected difficulty level.

    Provides feedback on guesses, indicating if they are too small or too large.

    Ensures that all guesses are positive integers and handles invalid inputs gracefully.

**Sample Interactions:**

    Level: 1
    Guess: 5
    Too small!
    Guess: 9
    Too large!
    Guess: 7
    Just right!

### **4. adieu.py**

**Description**

adieu.py generates a farewell message for a list of names. Using the inflect library, it formats the names grammatically( with an ***[oxford comma] (https://en.wikipedia.org/wiki/Serial_comma)*** )into a well-structured sentence.

**Features**

    Accepts a list of names entered one at a time.

    Ends input collection upon CTRL+D (EOF).

    Formats names using the inflect library for proper grammar.

**Sample Input:**

    Name: Alice
    Name: Bob
    Name: Charlie
    [CTRL+D]

**Expected Output:**

    Adieu, adieu, to Alice, Bob, and Charlie

### **5. figlet.py**

**Description**

figlet.py converts user input text into ASCII art using the pyfiglet library. Users can optionally specify a font or rely on a randomly chosen font.

**Features**

    Accepts optional command-line arguments to specify a font.

    Renders text as ASCII art with a wide range of fonts.

    Handles invalid font names and invalid usage gracefully.

Sample Input:
    $ python figlet.py
    Input: Hello
Expected Output:

    _   _      _ _
    | | | |    | | |
    | |_| | ___| | | ___
    |  _  |/ _ \ | |/ _ \
    | | | |  __/ | | (_) |
    \_| |_/\___|_|_|\___/


### **6. emojize.py**

**Description**

emojize.py converts text containing emoji aliases into their corresponding emojis, allowing for creative and expressive outputs.

**Features**

    Prompts users to input text containing emoji 'codes' or their aliases (e.g., :smile: , :thumbs_up:).

    Uses the emoji library to translate aliases into emojis.

**Sample Input:**

    Input: I love :pizza: and :coffee:!

**Expected Output:**

    Output: I love 🍕 and ☕!

Feel free to clone or fork this repository and contribute to these problem sets by adding more scenarios or enhancing the existing ones.