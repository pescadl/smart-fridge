from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/list')
def list():
    return render_template('list.html')

@app.route('/list')

@app.route('/recipe')
def recipe():
    return render_template('recipe.html')

if __name__ == "__main__":
    app.debut = True
    app.run()
