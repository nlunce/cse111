import csv

def main():

    I_NUMBER_INDEX = 0
    NAME_INDEX = 1

    student_dict = read_dict('students.csv', I_NUMBER_INDEX)
    
    inum_input = input('\nPlease enter an I-Number (xxxxxxxxx): ')
    if inum_input in student_dict:
        print(f'\nStudent Name: {student_dict[inum_input][NAME_INDEX]}')
    else:
        print('\nNo such student')
    

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    student_dict = {}
    with open(filename, 'rt') as file:
        
        csvreader = csv.reader(file)
        next(csvreader)
        for row_list in csvreader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                student_dict[key] = row_list
            
    
    return student_dict

if __name__ == "__main__":
    main()