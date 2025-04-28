import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sonu@1234",
    database="db1")
c=conn.cursor()

sid=input("Enter your id to delete record from Student")

c.execute("delete from student where sid=%s",(sid,))
conn.commit()
c.close()
conn.close()
