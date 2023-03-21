def empty(data):
    removed_empty = []

    for line in data:
        if all(col.strip() for col in line):
            removed_empty.append(line)
        
    
    return(removed_empty)
