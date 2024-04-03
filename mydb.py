import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user = 'userName',
    passwd = 'yourPassword',

)

cursorObject = db.cursor()

cursorObject.execute("CREATE DATABASE kreative")

print("All done!")
