from Database_Connect import database_connector
from tabulate import tabulate

mydb = database_connector()
mycursor = mydb.cursor()


class Owner:
    """Class for Object of type 'Owner'. Contains all the functions accessible by an Owner."""

    def __init__(self, name):
        """Function to initiate an Owner and add it to the Owners table if it doesn't exist."""

        Owner.name = name
        Owner.purAmount = 0
        Owner.totBalance = 0
        mycursor.execute("SELECT OWNER_ID, NAME FROM OWNERS")
        myresult = mycursor.fetchall()
        if myresult == []:
            x = [0, None]

        owners = []
        for x in myresult:
            owners.append(x[1])

        if Owner.name not in owners:
            id = x[0] + 1
            mycursor.execute(
                f"INSERT INTO OWNERS VALUES({id}, '{Owner.name}', {Owner.totBalance})")

        mydb.commit()

    @staticmethod
    def Stock_Report():
        """Static Funtion to print the Stock Report."""

        mycursor.execute("SELECT * FROM STOCK;")
        myresult = mycursor.fetchall()
        if mycursor.rowcount == -1:
            print("There is no stock left!")
        else:
            print(tabulate(myresult, headers=[
                "Sr. No.", "Item Name", "Cost Price", "Selling Price", "Stock Left", "Unit"], tablefmt='fancy_grid'))

    @staticmethod
    def ItemIsThere(sr="", name=""):
        """Static Function to search for an Item using it's Sr. No. or Name. Return True/False."""

        mycursor.execute("SELECT SRNO, ITEM_NAME FROM STOCK;")
        srList = []
        itemList = []
        for i in mycursor:
            srList.append(i[0])
            itemList.append(i[1].lower())

        if sr in srList or name.lower() in itemList:
            return True
        else:
            return False

    def Show_Customers(self):
        """Function that prints Customers table from Database."""

        mycursor.execute(
            f"SELECT CUSTOMERS.ID, CUSTOMERS.NAME, PHONE, EMAIL, CUSTOMERS.ACCOUNT FROM CUSTOMERS, OWNERS WHERE CUSTOMERS.OWNER_ID = OWNERS.OWNER_ID AND OWNERS.NAME = '{Owner.name}';")
        myresult = mycursor.fetchall()
        if mycursor.rowcount == -1:
            print("There are no Customers for this Owner!")
        else:
            print(tabulate(myresult, headers=[
                  "Sr. No.", "Name", "Phone", "Email", "Account"], tablefmt='fancy_grid'))

    def Show_Owners(self):
        """Function that prints Owners Table from Database."""

        mycursor.execute("SELECT * FROM OWNERS;")
        myresult = mycursor.fetchall()
        if mycursor.rowcount == -1:
            print("Please add an Owner first!")
        else:
            print(tabulate(myresult, headers=[
                  "Sr. No.", "Name", "Account"], tablefmt='fancy_grid'))

    def P_Invoice(self):
        """Function to make Purchase for New Stock."""

        try:
            Owner.purAmount = 0
            NoOfItems = int(input("Enter No. Of Items to be Purchased :- "))
            for i in range(NoOfItems):
                srno = int(input("Enter Serial No. Of Item :-"))

                if Owner.ItemIsThere(srno):
                    mycursor.execute(
                        f"SELECT STOCK_LEFT, CP FROM STOCK WHERE SRNO = {srno}")
                    myresult = mycursor.fetchone()
                    qty = myresult[0]
                    cp = myresult[1]
                    Units_purchased = int(
                        input("Enter No. Of Units Purchased :-"))
                    qty = int(qty) + Units_purchased
                    mycursor.execute(
                        f"UPDATE STOCK SET STOCK_LEFT = {qty} WHERE SRNO = {srno}")
                    Owner.purAmount += (cp * Units_purchased)

                else:
                    item_name = input("Enter Item Name :-")
                    CP = int(input("Enter Cost Price/Unit Item :-"))
                    SP = int(input("Enter Selling Price/Unit Item :-"))
                    Units_purchased = int(
                        input("Enter No. Of Units Purchased :-"))
                    UnitOfItem = input("Enter Unit :-")

                    query = f"INSERT INTO STOCK VALUES({srno}, '{item_name}', {CP}, {SP}, {Units_purchased}, '{UnitOfItem}')"
                    mycursor.execute(query)
                    Owner.purAmount += (CP * Units_purchased)

                mydb.commit()
            mycursor.execute(
                f"SELECT ACCOUNT FROM OWNERS WHERE NAME = '{Owner.name}'")
            myresult = mycursor.fetchall()
            Owner.totBalance = myresult[0][0]
            print(f"{Owner.name} needs to pay Rs. {Owner.purAmount}")
            Owner.totBalance -= Owner.purAmount
            mycursor.execute(
                f"UPDATE OWNERS SET account = {Owner.totBalance} WHERE name = '{Owner.name}'")
            mydb.commit()

        except Exception as e:
            print(e)

    def account(self):
        """Function that prints the Amount in selected Owners Account."""

        mycursor.execute(
            f"SELECT NAME, ACCOUNT FROM OWNERS WHERE NAME = '{Owner.name}'")
        myresult = mycursor.fetchone()
        Owner.totBalance = myresult[1]
        print(f"{Owner.name} has Rs. {Owner.totBalance} in account!")

    def addCustomer(self, name):
        """Function to add a New Customer to Customers Table."""

        mycursor.execute("SELECT OWNER_ID, NAME FROM OWNERS")
        myresult = mycursor.fetchall()
        Owners = {}

        for x in myresult:
            Owners[x[1]] = x[0]

        for i in Owners:
            if Owner.name == i:
                id = Owners[i]

        phone = int(input("Enter Phone No. :-"))
        email = input("Enter Email Id :-")
        mycursor.execute(
            f"INSERT INTO CUSTOMERS(NAME, PHONE, EMAIL, OWNER_ID) VALUES('{name}','{phone}','{email}', {id});")
        mydb.commit()

    def delete_item(self):
        """Function to Delete Items from the Stock Table."""

        mycursor.execute("SELECT srno, item_name from stock")
        myresult = mycursor.fetchall()
        stock = {}
        print(tabulate(myresult, headers=[
              "Sr. No.", "Item"], tablefmt="fancy_grid"))
        for x in myresult:
            stock[x[0]] = x[1]
        while True:
            sr = int(input("Enter the Sr. No. of Item you want to Delete:-"))
            if sr not in stock:
                print("Please Enter a correct Sr. No. !")
            else:
                srno = sr
                item_name = stock[sr]
                if Owner.ItemIsThere(srno, item_name):
                    mycursor.execute(f"DELETE FROM STOCK WHERE SRNO = {srno}")
                    mydb.commit()
                    print("Item Deleted!")
                else:
                    print(
                        f"No Item named {item_name} is present in the Stock!")

            ans = input("Do you want to delete more items ? (Y/N):-")

            if ans not in 'Yy':
                break
