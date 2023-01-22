import sqlite3 



##Save Log in Data with SQLPython

##conn = sqlite3.connect('facebook.db')
##cursor = conn.cursor()
##
##cursor.execute("CREATE TABLE IF NOT EXISTS Users (ID INTEGER NOT NULL, Email TEXT NOT NULL, Password TEXT NOT NULL, Friends INTEGER NOT NULL)")
##
##cursor.execute("INSERT INTO Users VALUES(1,'ca@vengers.com','imOld', 65 )")
##cursor.execute("INSERT INTO Users VALUES(2,'spider@vengers.com','Peter', 117 )")
##cursor.execute("INSERT INTO Users VALUES(3,'iron@vengers.com','Tony', 500 )")
##cursor.execute("INSERT INTO Users VALUES(4,'hulkl@vengers.com','Dcotor', 20 )")
##
##user_email = input('Enter your Email: ')
##user_pass = input('Enter password: ')
##cursor.execute("SELECT * FROM Users WHERE Email = :email",{'email' : user_email})
##user = cursor.fetchone()
##if user is not None and user[2] == user_pass:
##    print('Welcome!')
##else:
##    print('Invalid User Email or Password.')




