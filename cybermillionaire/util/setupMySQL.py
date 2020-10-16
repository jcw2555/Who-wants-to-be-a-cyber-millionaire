"""
This file runs teh pulltsv.sh script, then access the local mySQL database, then runs import.sql
"""
import subprocess
import mysql.connector


#Call script to pull down questions
#subprocess.call("cybermillionaire/util/pulltsv.sh")




#Opens connection to mysql database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "RedBusStopsHere9" #change to local database password
    )
  
  
mycursor = mydb.cursor()

"""
mycursor.execute("show databases;")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
"""
mycursor.execute("\. cybermillionaire/util/import.sql", None, multi=False) #path to import.sql



