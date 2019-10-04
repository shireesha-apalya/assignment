import MySQLdb
db1 = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="shireesha",         # your username
                     passwd="M@rtins18",  # your password
                     db="test")        # name of the data base
db2 = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="nayini",         # your username
                     passwd="Password@123",  # your password
                     db="sample")

cur1 = db1.cursor()
print(cur1)
cur2 = db2.cursor()
print(cur2)
cur1.execute("select * from employee where user_id>=6 and user_id<=10")
rows = cur1.fetchall()
print(rows)
for row in rows:
    print(row)
    user_id = row[0]
    circle_id = row[1]
    query = "update employee set circle_id='{}' where user_id={};".format(circle_id,user_id)
    print("query:", query)
    b = cur2.execute(query)
    print(b)
    db2.commit()

db1.close()
db2.close()