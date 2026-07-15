import pymysql

mydb=pymysql.connect(host='localhost',user='root',password='root',database='python400')
mycursor=mydb.cursor()

while True:
    print("""
Press 1 to add data
press 2 to fetch data
press 3 to update data
press 4 to delete data
""")
    ch=int(input("Enter your choice: "))
    if ch==1:
        name=input("Enter the name: ")
        price=int(input("Enter the price: "))
        duration=int(input("Enter the duration: "))

        query="insert into java(name,price,duration) values ('%s','%s','%s')"
        args=(name,price,duration)
        mycursor.execute(query%args)
        mydb.commit()
        
    elif ch==2:
        query="select * from java"
        mycursor.execute(query)
        data=mycursor.fetchall()
        print(data)
        
    elif ch==3:
        