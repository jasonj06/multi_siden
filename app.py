import random

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# A view
@app.route("/", methods=['GET', 'POST'])
def sitemap():
    return render_template('home.html')

@app.route("/add", methods=['GET', 'POST'])
def add():  
    a = 0
    b = 0
    c = None
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        c = int(a)+int(b)
        
    return render_template('add.html', result=c, a1=a, b1=b) 

@app.route('/bmi_beregner', methods=['GET', 'POST'])
def bmi_beregner():
    return render_template('bmi_beregner.html')
                       


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)