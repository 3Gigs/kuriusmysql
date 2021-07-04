import mysql.connector

print("Enter username")
username = input()
print("Enter password")
password = input()

mydb = mysql.connector.connect(
  host="localhost",
  user=username,
  password=password
)

database = mydb.cursor(buffered=True)
database.execute("CREATE DATABASE IF NOT EXISTS kurius_mysql")
database.execute("USE kurius_mysql")
database.execute("""CREATE TABLE IF NOT EXISTS tasks(
  id INT AUTO_INCREMENT PRIMARY KEY,
  `task` VARCHAR(255) NOT NULL, 
  `desc` VARCHAR(255) NOT NULL
)""")

def insert_task():
  print("Enter a task")
  task = input()
  print("Enter task description")
  desc = input()
    
  sql = "INSERT INTO tasks (`task`, `desc`) VALUES (%s, %s)"
  row = (task, desc)
  database.execute(sql, row)
  mydb.commit()

  print(database.rowcount, """Record inserted, 
  the task ID is: """, database.lastrowid)

def select_task():
  database.execute("SELECT * FROM tasks")
  print("What to do? (Type DELETE, WHERE, FETCH, GO_BACK)")
  select_action = input()

  if(select_action == "DELETE"):
    print("Select task to delete")
    deleteQuery = input()
    sql = f"DELETE FROM tasks WHERE task='{deleteQuery}'"
    database.execute(sql)
    mydb.commit()
    print(database.rowcount, "record delete")
  if(select_action == "WHERE"):
    print("Search for task")
    taskQuery = input()
    sql = f"SELECT * FROM tasks WHERE task ='{taskQuery}'"
    database.execute(sql)
    whereResult = database.fetchall()
    for x in whereResult:
      print(x)
  if(select_action == "FETCH"):
    fetchResult = database.fetchall()
    for x in fetchResult:
      print(x)
  if(select_action == "GO_BACK"):
    pass

print("Welcome to tasks manager. ")
while True:
  print("What do you want to do? (Type INSERT, SELECT)")
  action = input()
  if(action == "INSERT"):
    insert_task()
  if(action == "SELECT"):
    select_task()