import csv

with open("students.csv", mode='r') as infile:
    reader = csv.reader(infile)
    with open('students_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1] for rows in reader}
            