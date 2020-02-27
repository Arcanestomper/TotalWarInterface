from flask import Flask, request, render_template, redirect, url_for

import sqlite3 
import SQLExample
import StatisticFunctions

# connecting to the database  
connection = sqlite3.connect("myTable.db") 
  
# cursor  
crsr = connection.cursor() 
#Ensure that the statistic table exists
SQLExample.CreateStatisticTable(crsr)

# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
connection.commit() 
  
# close the connection 
connection.close() 

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)
app.config["DEBUG"] = True

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

@app.route('/')
@app.route('/hello')
def index():
    # Render the page
    return '''
                <html>
                    <body>
                        <p>"Hello Python!"</p>
                        <p><a href="/TotalWar">Click here for the Total War interface</a>
                    </body>
                </html>
            '''

@app.route('/Test')
def Test():
    return redirect(url_for('UpdateStat'))

@app.route('/TestForm/')
@app.route('/TestForm/<username>')
def TestForm(name=None):
    return render_template('TestForm.html', username=name)

@app.route('/Adder/', methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        number1 = None
        number2 = None
        try:
            number1 = float(request.form["number1"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number1"])
        try:
            number2 = float(request.form["number2"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number2"])
        if number1 is not None and number2 is not None:
            result = number1 + number2
            return '''
                <html>
                    <body>
                        <p>The result is {result}</p>
                        <p><a href="/Adder">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(result=result)
    return '''
        <html>
            <body>
                {errors}
                <p>Enter your numbers:</p>
                <form method="post" action=".">
                    <p><input name="number1" /></p>
                    <p><input name="number2" /></p>
                    <p><input type="submit" value="Do calculation" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)

@app.route('/TotalWar/', methods=["GET", "POST"])
def TW_Interface():
    errors = ""
    if request.method == "POST":
        Option = None
        try:
            Option = float(request.form["Option"])
        except:
            errors += "<p>{!r} is not an option.</p>\n".format(request.form["Option"])
        print(Option)
        if Option == 1:
            print(Option)
            #StatisticFunctions.UpdateFactionStats()
            return redirect(url_for('UpdateStat'))
        elif Option == 2:
            print(Option)
            #StatisticFunctions.DisplayAllStats()
            return redirect(url_for('DisplayAllStat'))
        elif Option == 3:
            print(Option)
            #StatisticFunctions.DisplayFactionStats()
            return redirect(url_for('DisplayFactionStat'))
        elif Option == 4:
            print(Option)            
            return redirect(url_for('DeleteFaction'))

    return '''
        <html>
            <body>
            {error}
                <p>Choose Operation:</p>
                <form method="post" action=".">
                    <input type="radio" id="Update" name="Option" value="1" checked>
                    <label for="Update">Update Stat</label><br>
                    <input type="radio" id="DisplayAll" name="Option" value="2">
                    <label for="DisplayAll">Display Statistics (All)</label><br>
                    <input type="radio" id="DisplayFaction" name="Option" value="3">
                    <label for="DisplayFaction">Display Statistics (Faction)</label><br>
                    <input type="radio" id="DeleteFaction" name="Option" value="4">
                    <label for="DeleteFaction">Remove a Faction</label><br>
                    <p><input type="submit" value="Submit Operation" /></p>
                </form>
            </body>
        </html>
    '''.format(error=errors)
    

@app.route('/UpdateStat/', methods=["GET", "POST"])
def UpdateStat ():
    if request.method == "POST":
        fname = str(request.form["fname"])
        ftype = str(request.form["ftype"])
        ftier = int(request.form["ftier"])
        fstat = str(request.form["stat"])
        newvalue = int(request.form["newvalue"])
        print (fname)
        print (ftype)
        print (ftier)
        print (fstat)
        print (newvalue)
        StatisticFunctions.UpdateFactionStats(fname, ftype, ftier, fstat, newvalue)
        return redirect(url_for('TW_Interface'))
    #    #fname,ftype,ftier,stat,newvalue
    return render_template('StatUpdate.html')

@app.route('/StatisticDisplayAll', methods=["GET", "POST"])
def DisplayAllStat ():
    rows = StatisticFunctions.DisplayAllStats()
    #    #fname,ftype,ftier,stat,newvalue
    return render_template('StatView.html', rows=rows)

@app.route('/StatisticDisplayFaction/', methods=["GET", "POST"])
def DisplayFactionStat ():
    if request.method == "POST":
        fname = str(request.form["fname"])
        rows = StatisticFunctions.DisplayFactionStats(fname)
        print(rows)
        return render_template('StatView.html', rows=rows)
    #    #fname,ftype,ftier,stat,newvalue
    return render_template('FactionSelection.html')

@app.route('/DeleteFaction/', methods=["GET", "POST"])
def DeleteFaction ():
    if request.method == "POST":
        fname = str(request.form["fname"])
        verify = str(request.form["verify"])
        StatisticFunctions.DeleteFaction(fname, verify)
        return redirect(url_for('TW_Interface'))
    #    #fname,ftype,ftier,stat,newvalue
    return render_template('FactionSelection.html', delete=True)

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run(debug="True")


