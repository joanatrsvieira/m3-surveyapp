from extract import get_input
from duplicates import duplicates
from emptylines import empty
from capitalize import capital
from validate import validate
from output import output
from outputprint import print_data
import csv

def test_input_is_correct():
    # Arrange
    filename = "results.csv"
    expected_output = ["user_id","first_name","last_name","answer_1","answer_2","answer_3"]
    expected_number_of_lines = 25

    #Act
    output = get_input(filename)
    output_first_line = output[0]
    output_number_of_lines = len(output[1:])

    # Assert
    assert output_first_line == expected_output
    assert output_number_of_lines == expected_number_of_lines

def test_duplicates():
    # Arrange
    filename = "clean_results.csv"
    
    # Act
    with open(filename, 'r') as file:
        rows = file.readlines()[1:]  # skip header row
        output_number_of_rows = len(set(frozenset(row.strip().split(',')) for row in rows))

    # Assert
    expected_number_of_rows = len(rows)
    assert output_number_of_rows == expected_number_of_rows


def test_empty():
    # Arrange
    filename = "clean_results.csv"
    expected_no_empty = True
    
    # Act
    with open(filename, 'r') as file:
        rows = file.readlines()[1:]  # skip header row
        output_no_empty = not any(',' not in row.strip() for row in rows)

    # Assert
    assert output_no_empty == expected_no_empty


def test_capital():
    # Arrange
    filename = "clean_results.csv"
    expected_capitalised = True

    # Act
    with open(filename, 'r') as file:
        rows = file.readlines()[1:]  # skip header row
        output_capitalised = all(all(value[0].isupper() for value in row.strip().split(',')[1:3]) for row in rows)

    # Assert

    assert output_capitalised == expected_capitalised, "Not all values are capitalized"



def test_validation():
    # Arrange
    filename = "clean_results.csv"
    expected_validation = True
    
    # Act
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            answer_3 = int(row['answer_3'])
            if not 1 <= answer_3 <= 10:
                output_validation = False
                break
        else:
            output_validation = True

    # Assert
    assert output_validation == expected_validation, "Validation failed"
