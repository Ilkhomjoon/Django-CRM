import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user = 'root',
    passwd = 'Ilhomjon0611',

)

cursorObject = db.cursor()

cursorObject.execute("CREATE DATABASE kreative")

print("All done!")