# store-management-system
An Intermediate Level Python - MySQL Connectivity based project. Contains various functions of a Store-Management-System. 

Help on module Main:

NAME
    Main

FUNCTIONS
    CustomerMenu()
        Function that shows the options for customers to select from.
    
    Menu()
        Function that show options to Log In as a Customer or an Owner or to Exit the program.
    
    OwnerMenu()
        Function that shows a Menu to select options from for the Owner of the Store.
        
Help on module Database_Connect:

NAME
    Database_Connect

FUNCTIONS
    create_tables()
        Function that creates the required tables in MySQL Database if not created already.

    database_connector()
        Function that Returns an Connection Object that connects Python to MySQL.
        
Help on module Owner:

NAME
    Owner

CLASSES
    builtins.object
        Owner

    class Owner(builtins.object)
     |  Owner(name)
     |
     |  Class for Object of type 'Owner'. Contains all the functions accessible by an Owner.
     |
     |  Methods defined here:
     |
     |  P_Invoice(self)
     |      Function to make Purchase for New Stock.
     |
     |  Show_Customers(self)
     |      Function that prints Customers table from Database.
     |
     |  Show_Owners(self)
     |      Function that prints Owners Table from Database.
     |
     |  __init__(self, name)
     |      Function to initiate an Owner and add it to the Owners table if it doesn't exist.
     |
     |  account(self)
     |      Function that prints the Amount in selected Owners Account.
     |
     |  addCustomer(self, name)
     |      Function to add a New Customer to Customers Table.
     |
     |  delete_item(self)
     |      Function to Delete Items from the Stock Table.
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  ItemIsThere(sr='', name='')
     |      Static Function to search for an Item using it's Sr. No. or Name. Return True/False.
     |
     |  Stock_Report()
     |      Static Funtion to print the Stock Report.
     
Help on module Customer:

NAME
    Customer

CLASSES
    builtins.object
        Customer

    class Customer(builtins.object)
     |  Customer(name)
     |
     |  Class for an Object of type 'Customer'. Contains all the functions accessible by a Customer.
     |
     |  Methods defined here:
     |
     |  S_Invoice(self)
     |      Function to generate a Sales Invoice for a Customer. Asks for items to be purchased from Customer and Prints Invoice.        
     |
     |  __init__(self, name)
     |      Function to initiate a Customer and add it to Customers Table if it doesn't exist.
     |
     |  payBill(self)
     |      Function to settle accounts by paying the outstanding bill.
     |
     |  printInvoice(self)
     |      Function to print the Sales Ivoice.
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  search_item(name)
     |      Static Function to search if a given item is there in stock or not.
     

This project can be used for Class 12th Computer Science Project as it serves the purpose correctly.
