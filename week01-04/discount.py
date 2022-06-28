import datetime

date = datetime.datetime.now()

weekday = date.strftime('%a').lower()

sales_tax = .06
discount = .1

subtotal = float(input('\nPlease enter the subtotal: $ '))


if (weekday == 'tue' or weekday == 'wed') and subtotal >= 50:
    discount_amount = subtotal *discount
    subtotal -= discount_amount
    sales_tax_amount = subtotal * sales_tax
    total= subtotal + sales_tax_amount
    print(f'Discount amount: ${discount_amount: .2f}\nSales tax amount: ${sales_tax_amount: .2f}\nTotal: ${total: .2f}')
else:
    sales_tax_amount = subtotal * sales_tax
    total= subtotal + sales_tax_amount
    print(f'Sales tax amount: ${sales_tax_amount: .2f}\nTotal: ${total: .2f}')



    







