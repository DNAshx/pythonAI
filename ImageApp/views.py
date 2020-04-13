from flask import Flask, render_template
from ImageApp import app

@app.route('/')
@app.route('/index')
def index():
     return render_template(
        "Main.html"
    )
@app.route('/hello')
def hello():
    # Render the page
    return "Hello Python!"