# Import Flask to allow us to create our app
from flask import Flask
#Create a new instance of the Flask class called "app"
app = Flask(__name__)

# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello World!' # Return the string as a "Hello World response"
if __name__ =="__main__": # Ensure this file is being run directly and not from a different module
    app.run(debug=True) # Run the app in debug mode.