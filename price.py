dict={'sugar':40,'flour':80,'rice':45,'milk':20,'salt':12}
list=['sugar','flour','rice','milk','salt']
print('list of items are ',list )
x = input('enter product name; ')
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

# print(dictprice)
print('\tProduct Name\tProduct Price')
for k,v in dictprice.items():
    print('\t{}\t\t${}'.format(k,v))

print('your total price: ',totalprice)
