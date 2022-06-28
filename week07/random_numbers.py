import random

def main():
    numbers_list = []
    append_random_numbers(numbers_list)
    print(numbers_list)
    append_random_numbers(numbers_list, 100000000)
    print(numbers_list)

def append_random_numbers(numbers_list, quantity=1):
 
    for i in range(quantity):
        number = random.uniform(0,1000)
        number = round(number, 1)
        numbers_list.append(number)
    return numbers_list

if __name__ == "__main__":
    main()







