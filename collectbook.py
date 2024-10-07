import mysql.connector

myConnection = mysql.connector.connect()

#print(myConnection)

#create new record = add new data into table
sqlInsertCommand = "INSERT INTO bookdata ( author, country, imageLink, language, link, pages, title, year)\
      VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"

val = ( "Butterbear", "Thailand", "butterbear.co.th", "Thai", "NongNeay.com", 3, "NoeyNoi School", 1993)

myCursor = myConnection.cursor()

myCursor.execute(sqlInsertCommand, val)
myConnection.commit()
print(myCursor.rowcount, "record inserted")

#json > list > tuple > loop list

