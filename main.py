from flask import Flask,render_template
import os
from app import routes

## IF PROBLEMS WITH CSS : DO CTRL+SHIFT+R ON CHROME (WIN)

app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/deuxieme_index_trop_long_a_taper_pour_le_test")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/bug")
def bug():
    return render_templ("bug.html")

@app.route("/salvador")
def salvador():
    return render_template("salvador.html")

if __name__ == "__main__":
    app.run(debug=True)
