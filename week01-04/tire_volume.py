import math
import datetime
date = datetime.datetime.now()
date = date.strftime('%Y-%m-%d')

buy_tires = ''

width = int(input('\nEnter the width of the tire in mm (ex 205): '))

aspect_ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))

diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter))/10000000000

print(f'\nThe approximate volume is{volume: .2f} liters')

while buy_tires != 'y' and buy_tires != 'n':
    buy_tires = input('\nWould you like to buy tires?: (y/n)')

if buy_tires == 'y':
    phone_number = input('\nWhat is your phone number? (ex: 000-000-0000): ')
    print('\nHave a nice day.')

    with open('volumes.txt', 'a') as file:
        file.write(f'{date}, {width}, {aspect_ratio}, {diameter}, {volume: .2f}, {phone_number}\n')
else:
    print('\nHave a nice day.')

    with open('volumes.txt', 'a') as file:
        file.write(f'{date}, {width}, {aspect_ratio}, {diameter}, {volume: .2f}\n')





 
  
