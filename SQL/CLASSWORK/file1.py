import pymysql

mydb=pymysql.connect(host='localhost',user='root',password='root')
mycursor=mydb.cursor()
mycursor.execute('create database if not exists python400')
mydb.commit()

mydb=pymysql.connect(host='localhost',user='root',password='root',database='python400')
mycursor=mydb.cursor()
mycursor.execute('create table if not exists java(id int primary key auto_increment,name varchar(50), price int,duration int)')
mydb.commit()

