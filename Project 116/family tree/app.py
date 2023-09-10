# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Pranav Rajesh" # write your name
    age = "14" # write your age

    return render_template('index.html' , d_name = name , d_age = age)

# define the route to father webpage
@app.route('/father')
def father():
    d_name = "Rajesh"
    d_age = 42
    return render_template('father.html',d_name= d_name, d_age = d_age)
# define the route to mother webpage
@app.route('/mother')
def mother():
    d_name = "Uma"
    d_age = 36
    return render_template('mother.html',d_name= d_name, d_age = d_age)

# define the route to friends webpage
@app.route('/friend')
def friend():
    d_name = "Scott"
    d_age = 15
    return render_template('friend.html',d_name= d_name, d_age = d_age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
