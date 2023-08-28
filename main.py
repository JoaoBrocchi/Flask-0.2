from flask import Flask
from flask import render_template
app = Flask(__name__)
import datetime
import requests
current_year  = datetime.datetime.today().year

age_guess = requests.get(f"https://api.agify.io?name=joao")
gender_guess = requests.get(f"https://api.genderize.io?name=joao")

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/blogs/<num>")
def get_blog(num):
    print(num)
    all_blogs = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blogs.html",posts=all_blogs)



app.run(debug=True)