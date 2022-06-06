import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/aboutus')
def aboutus():
    people = ["Luis", "Lucas", "Maurice"]
    return render_template('templatetest.html', nameOfPage="About Us", type="About Us", people=people,  url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    people = ["Luis", "Lucas", "Maurice"]
    return render_template('templatetest.html', nameOfPage="Hobbies", type="Our Hobbies", people=people,  url=os.getenv("URL"))
