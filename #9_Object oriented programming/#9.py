##3
# class Switch:
#     """Switcher-class, returns a Boolean."""
#     __mode = False

#     def get_mode(self):
#         return self.__mode

#     def switch_mode(self):
#         if self.__mode == False:
#             self.__mode = True
#         else:
#             self.__mode = False

# Lamp = Switch()
# print(Lamp.get_mode())
# Lamp.switch_mode()
# print(Lamp.get_mode())


##4 
# class Example:
#     pass
# Randomstuff = Example()
# Randomstuff.value = 'I got this.'
# print(Randomstuff.value)


##5 Example: Using class attributes
#-*- coding: cp1252 -*-

# class delievery:
#     """Class defines a delievery package"""
#     item = ""
#     name = ""
#     address = ""

# def addnew():
#     customer = input("Customer name:")
#     place = input("Delievery address:")
#     stuff = input("What is the package: ")

#     packet = delievery()
#     packet.item = stuff
#     packet.name = customer
#     packet.address = place
#     return packet

 
# def main():
 
#     round = []
#     total = int(input("How many packages?:"))

#     for i in range(0,total):
#         deliever = addnew()
#         round.append(deliever)

#     print("Drop-off places:")
   
#     for i in range(0,total):
#         print(round[i].name+":"+round[i].address+":"+round[i].item)

# if __name__ == "__main__":
#     main()

##6
# class Customer:
#     name = "John Johnsson"
#     total = 1000
#     paymenttype = "Masterexpress"
#     number = "1234-5678-9012345"

#     def printout(self):
#         print("Name: ", self.name)
#         print("Total: ", self.total)
#         print("Payment type: ", self.paymenttype)
#         print("Card/Bill number: ", self.number)

# Customer1 = Customer()
# Customer1.printout()


##7 Example: Using class methods
# -*- coding: cp1252 -*-
# class Cart:
#     """This class manages the shopping cart. """
#     shoppingcart = []
#     def addstuff(self):
#         esine = input('What will be added?: ')
#         self.shoppingcart.append(esine)
    
#     def checkout(self):
#         print('Following objects were added:')
#         for i in range(0, len(self.shoppingcart)):
#             print(self.shoppingcart[i], end = ' ')

# def main():
#     customer = Cart()
#     while True:
#         selection = input('Add more or go to checkout?: ')
#         if selection == 'checkout':
#             customer.checkout()
#             break
#         else:
#             customer.addstuff()
# if __name__ == '__main__':
#     main()


##11
# class Customer:
#     name = "John Johnsson"
#     total = 1000
#     paymenttype = "Masterexpress"
#     number = "1234-5678-9012345"

#     def printout(self):
#         print("Name: ", self.name)
#         print("Total: ", self.total)
#         print("Payment type: ", self.paymenttype)
#         print("Card/Bill number: ", self.number)

# class Regular(Customer):
#     bonuscard = 'ABCD-1234'
#     bonusaccount = 0
#     def bonusdata(self):
#         print('This client has', self.bonusaccount, 'bonus points.' )

# Dave = Regular()
# Dave.name = 'Dave Davidsson'
# Dave.printout()
# Dave.bonusdata()

##12.1
# class Customer:
#     name = "John Johnsson"
#     total = 1000
#     paymenttype = "Masterexpress"
#     number = "1234-5678-9012345"

#     def printout(self):
#         print("Name: ", self.name)
#         print("Total: ", self.total)
#         print("Payment type: ", self.paymenttype)
#         print("Card/Bill number: ", self.number)

# class VIPcustomer(Customer):
#     def printout(self):
#         print('VIP client data is confidential!')

# Madonna = VIPcustomer()
# Madonna.printout()

##12.2 Example: Class inheritance and overwriting
class Cart():
    """This class manages the shopping cart."""

    shoppingcart = []
    def addstuff(self):
        esine = input('What will be added?: ')
        self.shoppingcart.append(esine)

    def checkout(self):
        print('Following objects were added:')
        for i in range(0, len(self.shoppingcart)):
            print(self.shoppingcart[i], end = ' ')

class SmallCart(Cart):
    '''This is a small cart with limited space'''
    size = 2
    def checkout(self):
        print('Following was added: ')
        for i in range(0, self.size):
            print(self.shoppingcart[i])
        if len(self.shoppingcart) > self.size:
            print('Some items were left out.')

def main():
    customer = SmallCart()
    while True:
        selection = input('Add more or go to checkout?: ')
        if selection == 'checkout':
            customer.checkout()
            break
        else:
            customer.addstuff()

if __name__ == '__main__':
    main()

