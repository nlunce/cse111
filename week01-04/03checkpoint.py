def main():
    start = int(input('\nEnter the first odometer reading (miles): '))
    end = int(input('\nEnter the second odometer reading (miles): '))
    gallons = float(input('\nEnter the amount of fuel used (gallons): '))
    mpg = miles_per_gallon(start, end, gallons)
    lp100k = lp100k_from_mpg(mpg)
    print(f'\n{mpg: .2f} miles per gallon\n{lp100k: .2f} liters per 100 kilometers')

def miles_per_gallon(start, end, gallons):
    mpg = (end-start)/gallons
    return mpg

def lp100k_from_mpg(mpg):
    lp100k = 235.215/mpg
    return lp100k


main()



