from extract import get_input

def test_input_is_list():
    # Arrange
    filename = "results.csv"
    expected_output = list

    # Act
    output = get_input(filename)

    # Assert
    assert type(output) == expected_output

def test_input_is_correct():
    # Arrange
    filename = "results.csv"
    expected_output = ["user_id","first_name","last_name","answer_1","answer_2","answer_3"]
    expected_number_of_lines = 25

    #Act
    output = get_input(filename)
    output_first_line = output[0]
    output_number_of_lines = len(output[1:])

    # Arrange
    assert output_first_line == expected_output
    assert output_number_of_lines == expected_number_of_lines

