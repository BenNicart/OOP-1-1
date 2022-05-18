import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access  Driver (*.mdb, *.accdb)}; DBQ=C:\Users\jocelyn g. nicart\OneDrive\Documents\Database1.accdb;')
    print("Database is Connected")

except pyodbc.Error:
    print("Database is Not Connected")