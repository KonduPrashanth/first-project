dict={'sugar':40,'flour':80,'rice':45,'milk':20,'salt':12}
list=['sugar','flour','rice','milk','salt']
print('list of items are ',list )
x = input('enter product name: ')
print('its price is ',dict[x])
quantity=int(input('provide quanity in kg: '))
price=dict[x]*quantity
print(price)
dictprice={}
# print(type(price))
option=input('if want buy type yes:')
totalprice=0
totalprice=totalprice+price
dictprice[x]=price
if option=='yes':
    print('list of items are ',list )
    while True:
        x = input('enter product name; ')
        quantity=int(input('provide quanity in kg: '))
        y=dict[x]*quantity
        totalprice=totalprice+y
        dictprice[x]=y
        z=input('if you want to exit: ')
        if z=='yes':
            break
# create a company name and information
company_name = 'Big Bazar Mall.'
company_address = 'kachiguda....'
company_city = 'New Delhi'

# declare ending message
message = 'Thanks for shopping with us today!'

# create a top border
print('*' * 50)

# print company information first using format
print('\t\t{}'.format(company_name.title()))
print('\t\t{}'.format(company_address.title()))
print('\t\t{}'.format(company_city.title()))

# print a line between sections
print('=' * 50)

# print out header for section of items
print('\tProduct Name\tProduct Price')

# create a print statement for each item
for k,v in dictprice.items():
    print('\t{}\t\t${}'.format(k,v))

# print a line between sections
print('=' * 50)

# print out header for section of total
print('\t\t\tTotal')

# calculate total price and print out
print('\t\t\t${}'.format(totalprice))

# print a line between sections
print('=' * 50)

# output thank you message
print('\n\t{}\n'.format(message))

# create a bottom border
print('*' * 50)
