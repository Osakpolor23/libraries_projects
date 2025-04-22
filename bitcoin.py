# a program that gets the real-time market price of bitcoin through the CoinCap Bitcoin Price index API
# created my coincap account with https://pro.coincap.io/signup to get my coincap api key
# import libraries
import requests
import sys
import json

# if the user's input in the command-line is not one argument plus name of file
if len(sys.argv) != 2: 
    # exit program with this error message
    sys.exit("Missing command_line argument") 

# try the following
try:

    # get the response from the coincap API url and my api key
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=3fce909ae7ac6cab60ef37d96da2eb5f89936e671dd10ad8c956dead3307ce8b")

    
    # pass the response in json format and assign to variable o
    o = response.json()

    # access the value of price of bitcoin from the output which is in the dict "data" within the dict output
    # and convert to a float
    btc_price = float(o["data"]["priceUsd"])  

    # store the user's command-line input in number after converting to a float
    number = float(sys.argv[1])

    # get the amount of the number of bitcoins entered
    amount = btc_price * number

# if a connection error occurs while calling the API
except requests.RequestException:
    # output the error message and exit the program
    sys.exit("an error occurred while making the request")
# if an input other than a datatype convertible to a float is entered i.e non-numeric e.g text
except ValueError:
    # output the error message and exit the program
    sys.exit("command-line argument is not a number")

# print the bitcoin amount, separate every thousand with a comma, and output to 4dp
print(f"${amount:,.4f}")




