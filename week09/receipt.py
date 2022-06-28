import csv
import datetime

def main():

    try:
        date = datetime.datetime.now()
        date = date.strftime('%a %Y-%m-%d %I:%M:%S')
        PRODUCT_KEY_INDEX = 0
        REQUEST_QUANTITY_INDEX = 1
        PRODUCT_NAME_INDEX = 1
        PRODUCT_PRICE_INDEX = 2
        request_file = 'request.csv'
        products_file = 'products.csv'

        products_dict = read_dict(products_file, PRODUCT_KEY_INDEX)
        # print(f'\nAll Products\n\n{products_dict}')
        
        request_list = []
        with open(request_file, 'rt') as file:
            csvreader = csv.reader(file)
            next(csvreader)

            total_items = 0
            subtotal = 0
            for row in csvreader:
                item_list = []
                if row[PRODUCT_KEY_INDEX] in products_dict:
                    key = row[PRODUCT_KEY_INDEX]
                    item_list.append(row[REQUEST_QUANTITY_INDEX])
                    item_list.append(products_dict[key][PRODUCT_NAME_INDEX])
                    item_list.append(products_dict[key][PRODUCT_PRICE_INDEX])
                    request_list.append(item_list)
                    subtotal += float(products_dict[key][PRODUCT_PRICE_INDEX]) * float(row[REQUEST_QUANTITY_INDEX])
                    total_items += float(row[REQUEST_QUANTITY_INDEX])
                else:
                    raise KeyError
                
        sales_tax = subtotal * .06
        total = subtotal + sales_tax
        
        

        print(f'\nInkom Emporium\n')
        for i in range(len(request_list)):
            print(f'{request_list[i][1]}: {request_list[i][0]} @ ${request_list[i][2]}')
        print(f'\nNumber of Items: {total_items:.0f}\nSubtotal: ${subtotal:.2f}\nSales Tax: ${sales_tax:.2f}\nTotal: ${total:.2f}')
        print(f'\nThank you for shopping at the Inkom Emporium.\n{date}')
        print('\nFill out a customer satisfaction survey to recieve a\n10% discount on your next purchase:\nwww.survey.com')

    
    except PermissionError as perm_err:
        print(perm_err)
    except FileNotFoundError as not_found_err:
        print('File does not exist')
        print(not_found_err)
    except KeyError as key_err:
        print(f'Error: Unknown product ID in the request.csv file \'{row[PRODUCT_KEY_INDEX]}\'')
    






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

    dict = {}
    with open(filename, 'rt') as file:
        
        csvreader = csv.reader(file)
        next(csvreader)
        for row_list in csvreader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dict[key] = row_list
    return dict
    

if __name__ == '__main__':
    main()
