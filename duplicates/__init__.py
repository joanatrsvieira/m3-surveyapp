def duplicates(data):
    column1 = []
    removed_duplicates = []

    for i in range(len(data)):
        unique_rows = (data[i][0])
        if unique_rows not in column1:
            removed_duplicates.append(data[i])
        column1.append(unique_rows)
    
    return(removed_duplicates)
