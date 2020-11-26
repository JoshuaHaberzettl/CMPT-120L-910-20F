import logging
import argparse
parser = argparse.ArgumentParser(description="Displays the summation notation of a given number using logging.")
logging.basicConfig(format="%(message)s", level=logging.INFO)

#You wrote that this was considered poor practice, but didn't give an
#example of good practice for a positional argument, just an optional one
parser.add_argument("number", help="This is the number to be summed")   
args = parser.parse_args()

logging.info('The number recieved in argparse is: ' + args.number)

#Finds and returns the summation notation for the given number through recursion
def summation(number):
   return summation_recursive(number, 0)

def summation_recursive(number, current_total):
    current_total += number

    if number > 1:
        current_total = summation_recursive(number-1, current_total)

    return current_total


#Print using the logger
logging.info("The summation notation of %s is: %s.", args.number, summation(int(args.number)))