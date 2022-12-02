from flask import Flask,render_template
import app.services as s

app = Flask(__name__)
 
@app.route("/")
def home_view():
    return render_template("home.html")

@app.route("/")
def run():
    # s.automit()
    print("commited")
    return render_template("home.html")
