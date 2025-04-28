import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sonu@1234",
    database="db1")
c=conn.cursor()
c.execute("insert into student values(101,'Ram','Hyderabad',90)")
conn.commit()
c.close()
conn.close()
