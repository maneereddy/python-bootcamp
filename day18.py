import mysql.connector
mydata = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="8639488740",
    database="hospital"
)
mydb = mydata.cursor()
mydb.execute("CREATE TABLE doctor(name VARCHAR(255),id CHAR(10), patient INTEGER(20))")
mydb.execute("SHOW TABLES")
for j in mydb:
    print(j)

sql="INSERT INTO doctor(name,id,patient) VALUES(%s, %s, %s)"
values = [("manee","A","3"),
          ("vinod","B","4"),
          ("siva","C","6"),
          ("nagi","D","0")]
mydb.executemany(sql,values)
mydata.commit()
mydb.execute("SELECT * FROM doctor")
myresult = mydb.fetchall()
for x in myresult:
    print(x)
mydb.execute("SELECT * FROM doctor WHERE patient > 5")
result = mydb.fetchall()
for i in result:
    print(i)
mydb.execute("SELECT * FROM doctor WHERE patient = 0")
res = mydb.fetchall()
for i in res:
    print(i)
