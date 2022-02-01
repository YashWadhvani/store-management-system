from unicodedata import name
from unittest.main import main
import Database_Connect as dc
from Owner import Owner
from Customer import Customer


def OwnerMenu():
    """Function that shows a Menu to select options from for the Owner of the Store."""

    name = input("Enter Your Name :-")
    owner = Owner(name)
    while True:
        print('='*55)
        print('='*15, 'STORE MANAGEMENT SYSTEM', '='*15)
        print('='*55)
        print()
        print('='*16, 'WELCOME TO XYZ STORE!', '='*16)
        print()
        print(' '*12, f"Hello, {owner.name}! Have a Great Day!")
        print(' PLEASE SELECT AN OPTION FROM THE CHOICES GIVEN BELOW! ')
        print()
        print('1. Stock Report', end='\t \t \t')
        print('2. Purchase Items')
        print('3. Show Owners\' List', end='\t \t')
        print('4. Show Customers\' List')
        print('5. Show Account', end='\t \t \t')
        print('6. Search Item')
        print('7. Delete Item From Stock', end='\t')
        print('8. Exit')
        print()
        ch = int(input('Enter Your Choice :-'))
        if ch == 1:
            owner.Stock_Report()
        elif ch == 2:
            owner.P_Invoice()
        elif ch == 3:
            owner.Show_Owners()
        elif ch == 4:
            owner.Show_Customers()
        elif ch == 5:
            owner.account()
        elif ch == 6:
            name = input('Enter The name of the Item you are searching for :-')
            if Owner.ItemIsThere(name=name):
                print(f"{name} is there in Stock!")
            else:
                print(f"Sorry! We dont have {name} right now.")
        elif ch == 7:
            owner.delete_item()
        elif ch == 8:
            break
        else:
            print("Please Enter a correct Choice!")


def CustomerMenu():
    """Function that shows the options for customers to select from."""

    name = input("Enter Your Name :-")
    customer = Customer(name)
    while True:
        print('='*55)
        print('='*15, 'STORE MANAGEMENT SYSTEM', '='*15)
        print('='*55)
        print()
        print('='*16, 'WELCOME TO XYZ STORE!', '='*16)
        print()
        print(' '*12, f"Hello, {customer.name}! Have a Great Day!")
        print(' PLEASE SELECT AN OPTION FROM THE CHOICES GIVEN BELOW! ')
        print()
        print('1. Purchase Items', end='\t \t')
        print('2. Pay Outstanding Bill')
        print('3. Search Item', end='\t \t')
        print('4. Exit')
        ch = int(input('Enter Your Choice :-'))
        if ch == 1:
            customer.S_Invoice()
        elif ch == 2:
            customer.payBill()
        elif ch == 3:
            item = input("Enter the name of the item :-")
            customer.search_item(item)
        elif ch == 4:
            break
        else:
            print("Please Enter a correct Choice!")


def Menu():
    """Function that show options to Log In as a Customer or an Owner or to Exit the program."""

    dc.create_tables()
    while True:
        print('='*55)
        print('='*15, 'STORE MANAGEMENT SYSTEM', '='*15)
        print('='*55)
        print()
        print('='*16, 'WELCOME TO XYZ STORE!', '='*16)
        print(' PLEASE SELECT AN OPTION FROM THE CHOICES GIVEN BELOW! ')
        print()
        print('1. Log In as Owner', end='\t \t')
        print('2. Log In as Customer')
        print('3. Exit')
        print('='*55)
        ch = int(input("Enter Your Choice :-"))
        if ch == 1:
            OwnerMenu()
        elif ch == 2:
            CustomerMenu()
        elif ch == 3:
            print("Thanks for using this Program!")
            break
        else:
            print("Please Enter a correct Choice!")


if __name__ == "__main__":
    Menu()
