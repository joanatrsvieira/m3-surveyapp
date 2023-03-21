import csv

def output(data):
    with open('clean_results.csv', 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        for row in data:
            csv_writer.writerow(row)
        
        
