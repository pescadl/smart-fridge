from flask import Flask, render_template, request
import os, sqlite3

# create the application
app = Flask(__name__)

def connect_db():
    return sqlite3.connect('smartfridge.db')

def disconnect_db(con):
    con.commit()
    con.close()

# connect to database
con = connect_db()
cur = con.cursor()

# create tables
cur.execute('CREATE TABLE IF NOT EXISTS FRIDGE (ID INTEGER PRIMARY KEY AUTOINCREMENT, QUANTITY INTEGER NOT NULL, FOOD TEXT NOT NULL)')

# commit changes and close the database connection
disconnect_db(con)

def get_fridge_list():
    con = connect_db()
    cur = con.cursor()

    cur.execute('SELECT * FROM FRIDGE')
    fridgeList = cur.fetchall()

    disconnect_db(con)
    return fridgeList

def insert_food_into_fridge(foodName):
    con = connect_db()
    cur = con.cursor()

    cur.execute('SELECT ID FROM FRIDGE WHERE Food = ?)', (foodName))
    foodID = cur.fetchone()
    if foodID is None:
        cur.execute('INSERT INTO FRIDGE (ID, Quantity, Food) VALUES (?,?)', (1, foodName))
    else:
        cur.execute('UPDATE FRDIGE SET Quantity = (SELECT Quantity FROM FRIDGE WHERE ID = ?)+1', (foodID))

    disconnect_db(con)

# render the html files
@app.route('/')
@app.route('/list')
def list():
    return render_template('list.html')

@app.route('/fridge')
def fridge():
    return render_template('fridge.html', fridgeList=get_fridge_list())

@app.route('/recipe')
def recipe():
    return render_template('recipe.html')

@app.route('/scan', methods=['GET', 'POST'])
def scan():
    if request.method == 'POST':
        return render_template('scan.html', message_complete = 'Scan complete! Check your Fridge.')
    elif request.method == 'GET':
        return render_template('scan.html')

