from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "afjasfkja87"
@app.route('/')
def index():
    num = random.randrange(0,101)
    session['num'] = num
    print(session['num'])
    return render_template("index.html")

@app.route('/guess', methods=["POST"])
def guess(request):
    if int(session['num']) == int(request.form['guess']):
        result = True
    return render_template("index.html", result=result)

if __name__=="__main__":
    app.run(debug=True)