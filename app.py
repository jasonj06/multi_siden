import random
import requests
import json
from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = '1234'

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
    v = 0
    h = 0
    r = None
    error_ = None

    if request.method == 'POST':
        v = request.form['v']
        h = request.form['h']
        try:
            r = float(v)/float(h)**2
        except:
            try:
                float(v)
                float(h)
                h = 1.75
                r = float(v)/float(h)**2
                error_ = True
            except:
                error_ = True
                
    if "last_bmi" not in session:
        last_bmi = r
        session['last_bmi'] = last_bmi

    return render_template('bmi_beregner.html', result=r, v=v, h=h, error_=error_, last_bmi=session['last_bmi'])

@app.route('/enhedsomregner')
def enhedsomregner():
    return render_template('enhedsomregner.html')

@app.route('/text_utility', methods=['GET', 'POST'])
def text_utility():
    return render_template('text_utility.html')

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    return meme_large

@app.route('/random_meme', methods=['GET'])
def random_meme():
    meme_picture = get_meme()
    return render_template('random_meme.html', meme_picture=meme_picture)


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)