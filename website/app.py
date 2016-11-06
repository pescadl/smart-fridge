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
cur.execute('CREATE TABLE IF NOT EXISTS LIST (ID INTEGER PRIMARY KEY AUTOINCREMENT, QUANTITY INTEGER NOT NULL, FOOD TEXT NOT NULL)')
cur.execute('CREATE TABLE IF NOT EXISTS RECIPE_NAMES (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL)')
cur.execute('CREATE TABLE IF NOT EXISTS RECIPE_INGREDIENTS (ID INTEGER PRIMARY KEY AUTOINCREMENT, RECIPE_ID INTEGER NOT NULL, QUANTITY INTEGER NOT NULL, FOOD TEXT NOT NULL)')

# commit changes and close the database connection
disconnect_db(con)

def get_fridge_list():
    con = connect_db()
    cur = con.cursor()

    cur.execute('SELECT * FROM FRIDGE')
    fridgeList = cur.fetchall()

    disconnect_db(con)
    return fridgeList

def get_recipe_list():
    con = connect_db()
    cur = con.cursor()

    cur.execute('SELECT * FROM RECIPE_NAMES')
    recipeNameList = cur.fetchall()

    disconnect_db(con)
    return recipeNameList

def get_ing_list():
    con = connect_db()
    cur = con.cursor()

    cur.execute('SELECT * FROM RECIPE_INGREDIENTS')
    ingList = cur.fetchall()

    disconnect_db(con)
    return ingList

@app.route('/make_recipe', methods = ['POST', 'GET'])
def make_recipe():
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        numIng = int(request.form['numIng'])
            
        con = connect_db()
        cur = con.cursor()

        cur.execute("INSERT INTO RECIPE_NAMES (NAME) VALUES (?)", (recipe_name,))
        cur.execute("SELECT ID FROM RECIPE_NAMES WHERE NAME == ?", (recipe_name,))
        parentID = int(cur.fetchone()[0])

        #print(parentID) 
        #cur.execute('SELECT * FROM RECIPE_NAMES')
        #listy = cur.fetchall()
        #for index in range(len(listy)):
        #    print(listy[index])
        
        for index in range(1, numIng+1):
            cur.execute("INSERT INTO RECIPE_INGREDIENTS (RECIPE_ID, QUANTITY, FOOD) VALUES (?,?,?)", (parentID, request.form['q'+ str(index)], request.form['i'+ str(index)]))

        disconnect_db(con)

        return render_template('addrecipe.html')

        #for num in range(1, numIng):


#def get_recipes():

#def get_grocery_list():

#def scan_fridge():

#def insert_food_into_fridge(foodName):
#    con = connect_db()
#    cur = con.cursor()
#
#    cur.execute('SELECT ID FROM FRIDGE WHERE Food = ?)', (foodName))
#    foodID = cur.fetchone()
#    if foodID is None:
#        cur.execute('INSERT INTO FRIDGE (ID, Quantity, Food) VALUES (?,?)', (1, foodName))
#    else:
#        cur.execute('UPDATE FRDIGE SET Quantity = (SELECT Quantity FROM FRIDGE WHERE ID = ?)+1', (foodID))
#
#    disconnect_db(con)
 

# render the html files
@app.route('/')
@app.route('/list')
def list():
    return render_template('list.html')

@app.route('/fridge')
def fridge():
    return render_template('fridge.html', fridgeList=get_fridge_list())

@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    if request.method == 'POST':
        # you want to create a new recipe, so go the addrecipe page
        return render_template('addrecipe.html')
    elif request.method == 'GET':
        # print out the recipes like 
        return render_template('recipe.html', recipeNameList=get_recipe_list(), ingList=get_ing_list())

@app.route('/addrecipe', methods=['GET', 'POST'])
def addrecipe():
    if request.method == 'GET':
        return render_template('addrecipe.html')
    elif request.method == 'POST':
        make_recipe()
        return render_template('addrecipe.html');

@app.route('/scan', methods=['GET', 'POST'])
def scan():
    if request.method == 'POST':
        return render_template('scan.html', message_complete = 'Scan complete! Check your Fridge.')
    elif request.method == 'GET':
        return render_template('scan.html')

