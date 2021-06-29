
#1)
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "8639488740"
)
dbse = mydb.cursor()
dbse.execute("SHOW DATABASES")
for db in dbse:
   print(db)


#2)
mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd= "8639488740",
    database = "testdb"
)
dbse2= mydb.cursor()
dbse2.execute("CREATE TABLE Employer(name VARCHAR(255), dep VARCHAR(200))")
dbse2.execute("CREATE TABLE Student(name VARCHAR(255),scetion VARCHAR(10))")
sqlvalues = "INSERT INTO Employer(name,dep) VALUES (%s, %s)"
employee = ("manee","software engineer")
sqlvalues2= "INSERT INTO Student(name,section) VALUES (%s, %s)"
student2 = ("ram","a")
dbse2.execute(sqlvalues,employee)
dbse2.execute(sqlvalues2,student2)

mydb.commit()

#3)
data = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="8639488740",
    database = "naadatabase"
)
dbms = data.cursor()
dbms.execute("CREATE TABLE worker (name VARCHAR(255),mobile INTERGER(15))")
values = "INSERT INTO worker(name,mobile) VALUES (%s , %s)"
worker1 = ("vinod","9533464563")
worker2 = ("siva","123456789")
data.commit()
dbms = data.cursor()
dbms.excute("SELECT * FROM woekers")
result = dbms.fetchall()
for i in result:
    print(i)


