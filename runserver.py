import os
from ImageApp import app

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')

    try:
        PORT = int(os.environ.get('SERVER_PORT', '4449'))
    except ValueError:
        PORT = 4449

    app.run(HOST, PORT)
#from flask import Flask, render_template
# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
#app = Flask(__name__)

## Flask route decorators map / and /hello to the hello function.
## To add other resources, create functions that generate the page contents
## and add decorators to define the appropriate resource locators for them.

#@app.route('/')
#@app.route('/index')
#def index():
#     return render_template(
#        "Main.html"
#    )
#@app.route('/hello')
#def hello():
#    # Render the page
#    return "Hello Python!"

#if __name__ == '__main__':
#    # Run the app server on localhost:4449
#    app.run('localhost', 4449)