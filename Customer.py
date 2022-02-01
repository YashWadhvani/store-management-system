from Database_Connect import database_connector
from Owner import Owner
from tabulate import tabulate

mydb = database_connector()
mycursor = mydb.cursor()


class Customer:
    """Class for an Object of type 'Customer'. Contains all the functions accessible by a Customer."""

    def __init__(self, name):
        """Function to initiate a Customer and add it to Customers Table if it doesn't exist."""

        Customer.name = name
        Customer.amount = 0
        Customer.itemsPur = []
        mycursor.execute("SELECT ID, NAME FROM CUSTOMERS")
        myresult = mycursor.fetchall()
        if myresult == []:
            x = [0, None]
        customers = []
        for x in myresult:
            customers.append(x[1])
        if Customer.name not in customers:
            Owner.addCustomer(Owner.name, Customer.name)

    @staticmethod
    def search_item(name):
        """Static Function to search if a given item is there in stock or not."""

        if Owner.ItemIsThere(name=name):
            print(F"We got enough stock of {name}!")
        else:
            print(f"Sorry! We don't have {name} in stock.")

    def S_Invoice(self):
        """Function to generate a Sales Invoice for a Customer. Asks for items to be purchased from Customer and Prints Invoice."""

        print(f"Hello {Customer.name}!")
        mycursor.execute("SELECT srno, item_name from stock")
        stock = mycursor.fetchall()
        srn = []
        print(tabulate(stock, headers=["Sr. No.", "Item"], tablefmt="fancy_grid"))
        for x in stock:
            srn.append(x[0])

        try:
            while True:
                sr = int(input("Enter the Sr. No. of Item you want to Purchase:-"))
                if sr not in srn:
                    print("Please Enter a correct Sr. No. !")
                else:
                    for i in stock:
                        if sr == i[0]:
                            query = f"SELECT STOCK_LEFT, STOCK_UNIT, ITEM_NAME, SP FROM STOCK WHERE SRNO = {sr}"
                            mycursor.execute(query)
                            result = mycursor.fetchall()
                            print(
                                f"{result[0][0]} {result[0][1]} of {result[0][2]} Left")
                            qty = int(input("Enter the Quantity of Item:-"))
                            query = f"UPDATE STOCK SET STOCK_LEFT = {result[0][0] - qty} WHERE SRNO = {sr}"
                            mycursor.execute(query)
                            Customer.amount += (qty * result[0][3])
                            items = [result[0][2], result[0]
                                     [3], qty, (qty * result[0][3])]
                            Customer.itemsPur.append(items)
                    ans = input("Do you want to buy more Items? (Y/N):-")
                    if ans not in "Yy":
                        break
            mycursor.execute(
                f"SELECT account FROM OWNERS WHERE name = '{Owner.name}'")
            myresult = mycursor.fetchall()
            Owner.totBalance = myresult[0][0]
            Owner.totBalance += Customer.amount
            mycursor.execute(
                f"SELECT ACCOUNT FROM CUSTOMERS WHERE name = '{Customer.name}';")
            myresult = mycursor.fetchall()
            for x in myresult:
                amt = x[0]
            mycursor.execute(
                f"UPDATE CUSTOMERS SET ACCOUNT = {amt} + {Customer.amount} where name = '{Customer.name}';")
            mydb.commit()
            Customer.printInvoice()

        except:
            print("Sorry! We don't have enough stock!\nPlease Check again in a few days!")

    def printInvoice(self):
        """Function to print the Sales Ivoice."""

        print("="*14, "INVOICE", "="*14)
        print("="*37)
        print(tabulate(Customer.itemsPur, headers=[
              "Item", "cost", "Quantity", "Amount"], tablefmt="fancy_grid"))
        print("="*37)
        print()
        print(f"Dear {Customer.name}, Your Bill Amount = Rs. {Customer.amount}")

    def payBill(self):
        """Function to settle accounts by paying the outstanding bill."""

        mycursor.execute(
            f"SELECT ACCOUNT FROM CUSTOMERS WHERE NAME = '{Customer.name}';")
        myresult = mycursor.fetchall()
        for x in myresult:
            amt = x[0]
        print(
            f"Dear {Customer.name}, you have an outsanding of Rs. {amt} to be paid!")
        print("1. Pay Now Partially\t\t2. Pay Now Fully\t\t3. Pay Later")
        print("***Note : You will be charged 10% Extra if you opt to pay later!*** ")
        ch = int(input("Please Enter Your Choice :- "))
        if ch == 1:
            paid = int(input("Enter Amount :-"))
            amt -= paid
        elif ch == 2:
            amt = 0
        else:
            amt += (0.1*amt)

        mycursor.execute(
            f"UPDATE CUSTOMERS SET ACCOUNT = {amt} WHERE NAME = '{Customer.name}';")
        mycursor.execute(
            f"UPDATE OWNERS SET ACCOUNT = ACCOUNT + {amt} WHERE NAME = {Owner.name}")
        mydb.commit()
