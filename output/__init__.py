import csv

def output(data):
    with open('clean_results.csv', 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(['user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3'])  # write headers
        for row in data:
            csv_writer.writerow(row)
        
        
