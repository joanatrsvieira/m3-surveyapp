def get_input(filename):
    rows = []
    
    with open(filename, 'r') as f:
        for line in f.readlines():
            rows.append(line.strip().split(','))

    return rows
