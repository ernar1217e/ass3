from flask import Flask , render_template 
from localdata import *
import requests

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def homepages():
    return render_template('home.html',posts=postss,contac=contacts)

@app.route("/about")
def about():
    return render_template('about.html',title='About Us')

@app.route("/contact")
def contact():
    return "<p>+77755599922</p>"

@app.route('/user/<name>')
def user_profile(name):
    return render_template('user_profile.html',username=name)

@app.route("/alluser")
def all_user():
    userdata = requests.get('http://127.0.0.1:8000/users')
    print (userdata.json())
    return render_template('alluser.html',users=userdata.json())

if __name__ == "__main__":

    app.run(debug=True , port=5002)
