from msilib import Table
from multiprocessing import connection
from sqlite3 import DatabaseError
from turtle import hideturtle
from urllib import request
import jinja2
import mysql.connector as connection

class DBconnect:
    def __init__(self) -> None:
        self.con = connection.connect(host ='localhost',port = '3306', user ='root',password = 'maakelal', database ='py_mysql',autocommit=True)

# Create Table
        query = 'create table if not exists user1 (c_id int not null primary key, f_name varchar(40) not null, l_name varchar(40) not null, age int not null, phone varchar(13) not null)'
        var=self.con.cursor()
        var.execute(query)
# Insert Data in Table
    def ins(self,c_id,f_name,l_name,age,phone):
        query = "insert into user1 (c_id,f_name,l_name,age,phone) values ({},'{}','{}',{},'{}')".format(c_id,f_name,l_name,age,phone)
        var=self.con.cursor()
        var.execute(query)
        # self.con.commit()
        print ("user save to Database")

# fetch Data
    def fetch (self):
        query = 'select * from user1'
        var=self.con.cursor()
        var.execute(query)
        for row in var:
            print ("id :",row[0])
            print ("First Name :",row[1])
            print ("Last Name :",row[2])
            print ("Age :",row[3])
            print ("Phone :",row[4])
            print ("")


var = DBconnect()
# var.ins(2,"Mukesh","Kumar",26,"7870966936")
var.fetch()



