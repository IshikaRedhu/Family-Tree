#Importing flask module in the project
from flask import Flask

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/")

#‘/’ URL is bound with first_flask function.
def home():

    name : 'Alex'
    age : '11'
    return render_template('index.html' , name = name , age = age)

@app.route("/father")
def father():
    name = "Stephen"
    age = "39" 
    return render_template('father.html' , name = name , age = age)

@app.route("/mother")
def mother():
    name = "Diana"
    age = "37" 
    return render_template('mother.html' , name = name , age = age)


@app.route("/friend")
def friend():
    name = "George" 
    age = "11"
    return render_template('friend.html' , name = name , age = age)

if __name__  ==  '__main__':
    app.run(debug=True)
