def capital(data):
    with_capitalized = []
    for row in data:
        new_row = [row[0]] + [col.capitalize() for col in row[1:3]] + row[3:]
        with_capitalized.append(new_row)
    
    return(with_capitalized)