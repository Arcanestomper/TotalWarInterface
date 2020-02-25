
# Python code to demonstrate table creation and  
# insertions with SQL 
  
def SQLMain():
    # importing module 
    import sqlite3 
  
    print("Hello World This is SQL Example")
    # connecting to the database  
    connection = sqlite3.connect("myTable.db") 
  
    # cursor  
    crsr = connection.cursor() 
 
    CreateStatisticTable(crsr)
    targettable = "Statistics"
    
    #InsertStatisticTable(crsr, targettable, values)
    #fname = input("Faction Name: ")
    #type = input("Stat Type: ")
    #tier = input("Stat Tier: ")
    #NewStatRow(crsr, fname, type, tier)
    #UpdateStatisticTable(crsr, 1, "court", 20)

    ModifyStat(crsr,'House Purple','Production',1,'market',30)

    print("Final Table")
    DisplayTable(crsr,targettable)
    # To save the changes in the files. Never skip this.  
    # If we skip this, nothing will be saved in the database. 
    connection.commit() 
  
    # close the connection 
    connection.close() 

def CreateStatisticTable(cursor):
    import sqlite3
    print("CreateStatisticTable: Start")
    # SQL command to create a table in the database 
    sql_command = """CREATE TABLE Statistics (  
    findex INTEGER PRIMARY KEY,  
    faction VARCHAR(30),  
    type VARCHAR(20),  
    tier INTEGER,  
    navy INTEGER,
    agency INTEGER,
    market INTEGER,
    university INTEGER,
    court INTEGER);"""
  
    # execute the statement 
    try:
        cursor.execute(sql_command) 
    except sqlite3.OperationalError as err:
        print("CreateTable: OperationalError: {0}".format(err))

def InsertStatisticTable(cursor,table,values):
    import sqlite3
    print(InsertStatisticTable.__name__ + ": Start")
    #Find the last row
    index = 0
    sql_command = "SELECT * FROM "+ table
    try:
        cursor.execute(sql_command) 
    except sqlite3.IntegrityError as err:
        print("CreateTable: IntegrityError {0}".format(err)) 
 
    rows = cursor.fetchall()

    for row in rows:
        index = row[0]

    index = index +1
    istr = str(index)
    #Format SQL command
    sql_command_table = """INSERT INTO """ + table
    sql_command_values = """ VALUES (""" + istr +""", ?, ?, ?, ?, ?, ?, ?, ?);"""

    sql_command = sql_command_table + sql_command_values

    try:
        cursor.execute(sql_command, values) 
    except sqlite3.IntegrityError as err:
        print("CreateTable: IntegrityError {0}".format(err)) 

def NewStatRow(cursor,faction,type,tier):

    values = (faction, type, tier, 0, 0, 0, 0, 0)
    InsertStatisticTable(cursor,"Statistics",values)

def UpdateStatisticTable(cursor,findex,stat,newvalue):
    import sqlite3
    print(UpdateStatisticTable.__name__ + ": Start")

    #Format SQL command
    sql_command = str(""" UPDATE Statistics SET {1} = {2} WHERE findex = {0}""".format(findex,stat,newvalue))


    try:
        cursor.execute(sql_command) 
    except sqlite3.IntegrityError as err:
        print("CreateTable: IntegrityError {0}".format(err)) 

def ModifyStat(cursor,faction,type,tier,stat,newvalue):
    import sqlite3
    #print(ModifyStat.__name__ + ": Start")
    findex = 0
    #First find the correct row
    sql_command = str(""" SELECT findex FROM Statistics WHERE faction = '{0}' AND type = '{1}' AND tier = {2}""".format(faction,type,tier))
    #print(sql_command)
    try:
        cursor.execute(sql_command) 
    except sqlite3.IntegrityError as err:
        print("ModifyStat: IntegrityError {0}".format(err)) 
    except sqlite3.OperationalError as err:
        print("ModifyStat: OperationalError {0}".format(err)) 

    rows = cursor.fetchall()
    #If no row currently exists make one
    if len(rows) == 0:
        #print("Create new Row")
        NewStatRow(cursor,faction,type,tier)
        cursor.execute(sql_command)
        rows = cursor.fetchall()

    #Find the index
    #There should only be one    
    for row in rows:
        findex = row[0]
    #print(findex)
    UpdateStatisticTable(cursor,findex,stat,newvalue)

def SelectAllTable(cursor, table):
    import sqlite3
    sql_command = "SELECT * FROM "+ table
    try:
        cursor.execute(sql_command) 
    except sqlite3.IntegrityError as err:
        print("CreateTable: IntegrityError {0}".format(err)) 
 
    rows = cursor.fetchall()

    return rows

def DisplayTable(cursor, table):
    rows = SelectAllTable(cursor, table) 
    for row in rows:
        print(row)