import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sonu@1234",
    database="db1")
c=conn.cursor()

sid=input("Enter id")
sname=input("Enter name")
city=input("Enter city")
marks=input("Enter marks")


c.execute("insert into student values(%s,%s,%s,%s)",(sid,sname,city,marks))
conn.commit()
c.close()
conn.close()
