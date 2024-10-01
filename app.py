from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():

    return render_template("index.html")

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')


app.run(debug=True, host='0.0.0.0')