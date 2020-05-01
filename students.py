import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="school")
cursor = connection.cursor()
# Query for creating table
ID=2
sql1="UPDATE ATTENDANCE SET PRESENT_ABSENT='A'"
cursor.execute(sql1)

connection.commit()
connection.close()