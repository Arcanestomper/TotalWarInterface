import sqlite3
import SQLExample

def UpdateFactionStats(cursor):
    fname = input("Choose a Faction: ")
    #Faction does not have to be validated as a new faction will result in a new row
    validate = 0
    while validate < 5:
        print("1: Production")
        print("2: Prototype")
        ftype = input("Choose a Type: ")
        if ftype == "1" or ftype == "Production":
            ftype = "Production"
            break
        elif ftype == "2" or ftype == "Prototype":
            ftype = "Prototype"
            break
        else:
            validate = validate + 1
            print("Invalid Input: Attempts Remaining {0}".format(5 - validate))
    if validate == 5:
        print("Input Failed")
        return
    #Validate Type
    validate = 0
    while validate < 5:
        ftier = input("Choose a Tier: ")
        try:
            x = int(ftier) 
        except ValueError:
            validate = validate + 1
            print("Invalid Input: Attempts Remaining {0}".format(5 - validate))
        else:
            if x < 1:
                validate = validate + 1
                print("Invalid Input: Attempts Remaining {0}".format(5 - validate))
            else:
                break
    if validate == 5:
        print("Input Failed")
        return

    #Validate Stat
    while validate < 5:
        print("1: Navy")
        print("2: Agency")
        print("3: Market")
        print("4: University")
        print("5: Court")
        stat = input("Choose a Statistic: ")
        if stat == "1" or stat == "Navy":
            stat = "navy"
            break
        elif stat == "2" or stat == "Agency":
            stat = "agency"
            break
        elif stat == "3" or stat == "Market":
            stat = "market"
            break
        elif stat == "4" or stat == "University":
            stat = "university"
        elif stat == "5" or stat == "Court":
            stat = "court"
            break
        else:
            validate = validate + 1
            print("Invalid Input: Attempts Remaining {0}".format(5 - validate))
    if validate == 5:
        print("Input Failed")
        return
    #Validate Value
    validate = 0
    while validate < 5:
        newvalue = input("Choose a Value: ")
        try:
            x = int(newvalue) 
        except ValueError:
            validate = validate + 1
            print("Invalid Input: Attempts Remaining {0}".format(5 - validate))
        else:
            if x < 1:
                validate = validate + 1
                print("Invalid Input: Attempts Remaining {0}".format(5 - validate))
            else:
                break
    if validate == 5:
        print("Input Failed")
        return

    #All Validation Passed
    print("All Validation Passed")
    SQLExample.ModifyStat(cursor,fname,ftype,ftier,stat,newvalue)
    return

def DisplayAllStats(cursor):
    print("Displaying All Stats")
    rows = SQLExample.SelectAllTable(cursor,"Statistics")
    FormatDisplay(rows)

    return

def DisplayFactionStats(cursor):
    fname = input("Choose a Faction: ")
    #import sqlite3
    #sql_command = str(""" SELECT findex FROM Statistics WHERE faction = '{0}' AND type = '{1}' AND tier = {2}""".format(faction,type,tier))
    sql_command = str("""SELECT * FROM Statistics WHERE faction = '{0}'""".format(fname))
    #print(sql_command)
    try:
        cursor.execute(sql_command) 
    except sqlite3.IntegrityError as err:
        print("CreateTable: IntegrityError {0}".format(err)) 
 
    rows = cursor.fetchall()

    if len(rows)== 0:
        print("Invalid Faction")
        return

    FormatDisplay(rows)

def DeleteFaction(cursor):
    fname = input("Choose a Faction: ")
    verify = input ("Confirm Deletion of: {0} (Y/N)".format(fname))
    if verify == "Y":
        print("Deleting {0}".format(fname))
    else:
        print("Deletion Cancelled")
        return
    #import sqlite3
    #sql_command = str(""" SELECT findex FROM Statistics WHERE faction = '{0}' AND type = '{1}' AND tier = {2}""".format(faction,type,tier))
    #sql = 'DELETE FROM tasks WHERE id=?'
    sql_command = str("""DELETE FROM Statistics WHERE faction = '{0}'""".format(fname))
    #print(sql_command)
    try:
        cursor.execute(sql_command) 
    except sqlite3.IntegrityError as err:
        print("CreateTable: IntegrityError {0}".format(err)) 


def FormatDisplay(rows):

    #Display headers
    print(str("Faction").center(20), end='|')
    print(str("Type").center(15), end='|')
    print(str("Tier").center(6), end='|')
    print(str("Navy").center(6), end='|')
    print(str("Agency").center(8), end='|')
    print(str("Market").center(8), end='|')
    print(str("University").center(12), end='|')
    print(str("Court").center(7))

    #Display Rows
    for row in rows:
        print(str(row[1]).ljust(20), end='|')
        print(str(row[2]).ljust(15), end='|')
        print(str(row[3]).ljust(6), end='|')
        print(str(row[4]).ljust(6), end='|')
        print(str(row[5]).ljust(8), end='|')
        print(str(row[6]).ljust(8), end='|')
        print(str(row[7]).ljust(12), end='|')
        print(str(row[8]).ljust(7))

    return
