from flask import Flask, render_template
import os, sqlite3

# creat ethe application
app = Flask(__name__)

# connect to database
conn = sqlite3.connect('fridge.db')
cur = conn.cursor()

# create tables
cur.execute('CREATE TABLE FRIDGE (Quantity, Food, Expire)')
cur.execute('CREATE TABLE LIST (Quantiy, Food)')
cur.execute('CREATE TABLE RECIPE (Quantiy, Food)')

# commit and close the connetion to database
conn.commit()
conn.close()


# render the html files
@app.route('/', methods=['GET'])
@app.route('/list')
def list():
    return render_template('list.html')

@app.route('/fridge')
def fridge():
    return render_template('fridge.html');

@app.route('/recipe')
def recipe():
    return render_template('recipe.html')

@app.route('/scan')
def scan():
    return render_template('scan.html')

