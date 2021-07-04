import mysql.connector

print("Enter username")
username = input()
print("Enter password")
password = input()

mydb = mysql.connector.connect(
  host="localhost",
  user=username",
  password=password
)

print(mydb)