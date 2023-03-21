import csv
from extract import get_input
from duplicates import duplicates
from emptylines import empty
from capitalize import capital
from validate import validate
from output import output
from outputprint import print_data

def input(filename):
    data = get_input(filename)
    data=duplicates(data)
    data=empty(data)
    data=capital(data)
    data=validate(data)
    output(data)
    print('./clean_results.csv')
    return(data)

data=input('./results.csv')