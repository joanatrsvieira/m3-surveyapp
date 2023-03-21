def validate(data):
    validated = []
    for row in data:
        try:
            answer_row3 = int(row[5])
            if 1<= answer_row3 <=10:
                validated.append(row)
        except ValueError:
            pass
    
    return (validated)