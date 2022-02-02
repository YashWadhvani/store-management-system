import mysql.connector as mycon


def database_connector():
    """Function that Returns an Connection Object that connects Python to MySQL."""

    try:
        mydb = mycon.connect(
            host='localhost',
            user='root',
            password='', #Enter Your SQL Password here.
            database='STORE_MANAGEMENT'
        )

    except:
        mydb = mycon.connect(
            host="localhost",
            user="root",
            password="" #Enter Your SQL Password here.
        )
        mycursor = mydb.cursor()
        mycursor.execute('CREATE DATABASE STORE_MANAGEMENT')
        mydb.commit()

    return mydb


def create_tables():
    """Function that creates the required tables in MySQL Database if not created already."""

    mydb = database_connector()
    mycursor = mydb.cursor()
    mycursor.execute("USE STORE_MANAGEMENT")
    mycursor.execute("CREATE TABLE IF NOT EXISTS OWNERS(\
        OWNER_ID int primary key,\
        NAME varchar(20) not null,\
        ACCOUNT int not null)")
    mycursor.execute("CREATE TABLE IF NOT EXISTS STOCK(\
        SRNO int primary key,\
        ITEM_NAME varchar(20) not null,\
        CP int not null, SP int not null,\
        STOCK_LEFT int,\
        STOCK_UNIT varchar(10) not null)")
    mycursor.execute("CREATE TABLE IF NOT EXISTS CUSTOMERS(\
        ID int primary key,\
        NAME varchar(20) not null,\
        PHONE varchar(10) not null,\
        EMAIL varchar(60),\
        ACCOUNT int default 0,\
        OWNER_ID int not null,\
        FOREIGN KEY(OWNER_ID) REFERENCES OWNERS(OWNER_ID))")
    mydb.commit()
