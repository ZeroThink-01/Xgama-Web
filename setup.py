import os
import Xgamaversion
import main
from flask import send_from_directory
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')
    
@app.route('/invitesrc')
def invite():
    return render_template('invite&src.html')
    
@app.route('/license')
def license():
    return render_template('LICENSE.html')
    
@app.route('/versions')
def page_2():
    return render_template('page2.html')
    
@app.route('/contact')
def contact():
    return render_template('contact.html')
    
@app.route('/mostused')
def mostused():
    return render_template('mostused.html')
    
@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/lists')
def lists():
    return render_template('lists.html')
    
@app.route('/login2')
def login2():
    return render_template('login2.html')

if __name__ == '__main__':
    app.run(debug=True)
