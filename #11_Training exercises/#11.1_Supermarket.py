#11.1 Exercise: Supermarket
print('Supermarket\n===========')

totalsum = 0
while True:
    pricelist = [10,14,22,33,44,13,22,55,66,77]
    choice = int(input('Please select product (1-10) 0 to Quit: '))
    if choice == 0:
        print('Total: ', totalsum)
        payment = int(input('Payment: '))
        change = payment - totalsum
        print('Change:', change)
        break
            
    else:
        totalsum += pricelist[choice-1]
        print('Product: ', choice, 'Price: ', pricelist[choice-1])
        

    