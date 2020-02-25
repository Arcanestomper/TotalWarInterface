# importing module 
import sqlite3 
import SQLExample
import StatisticFunctions

# connecting to the database  
connection = sqlite3.connect("myTable.db") 
  
# cursor  
crsr = connection.cursor() 
#Ensure that the statistic table exists
SQLExample.CreateStatisticTable(crsr)

Interface = True
#Main Interface Loop
while Interface == True:
    print("==========================================================")
    print("==========================================================")
    print("1: Update Stat")
    print("2: Display Statistics (All)")
    print("3: Display Statistics (Faction)")
    print("4: Remove a Faction")
    print("Q: Close Interface")
    operation = input("Choose Operation: ")


    if operation == "1":
        StatisticFunctions.UpdateFactionStats(crsr)
    elif operation == "2":
        StatisticFunctions.DisplayAllStats(crsr)
    elif operation == "3":
        StatisticFunctions.DisplayFactionStats(crsr)
    elif operation == "4":
        StatisticFunctions.DeleteFaction(crsr)
    elif operation == "Q":
        Interface = False
    else:
        print("Invalid Operation")
#Exit Interface Loop
   
# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
connection.commit() 
  
# close the connection 
connection.close() 


