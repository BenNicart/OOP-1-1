import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver(*.mdb, *.accdb)}; DBQ=D:\Downloads\Database1.accdb;')
    print("Database is Connected")

    Fullname = "Ben Piolo G. Nicart"
    Age = 19
    Course = "BSCPE"
    Address = "General Trias"
    Grade = 99
    user_id = 10
    database = connection.cursor()
    database.execute('UPDATE Table1 sec Fullname=?, Age=?, Course=?, Address=?, Grade=? WHERE id=?',(user_id, Fullname, Age, Course, Address, Grade))
    connection.commit()
    print("Database is Updated")


except pyodbc.Error:
    print("Database is Not Connected")