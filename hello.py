from flask import Flask, render_template, request

#import <-- you can also use this istead of from ..

app = Flask("MyApp") #importing an app that's called "MyApp"

#roots is the relative path of the website, i.e. what's after the /

@app.route("/") #decorator .. before you do this code, do this other code
def hello():
	#hello method is the homepath, for example bbc.com
	return "Hello you!" 

@app.route("/<name>")
def hello_someone(name):
	return render_template("hello.html", name=name.title())

@app.route("/signup", methods=["POST"]) 
def sign_up():
	form_data = request.form
	print form_data["email"]
#This line tells the terminal to print the email in the command line.
	return "All OK"
#This line tells the webpage to change to the page called /signup, which is the @app.route("/signup", methods["POST"]) <-- POST tells you to give the server some information that you want to do something with. 

#app.run starts your application - otherwise it's not run
#without app.run it is waiting for interaction from visitors on the webpage

#copy link that the terminal gives you or put localhost:5000
# @app.route("/idontexist") #decorator .. before you do this code, do this other code
#def idontexist():
	#hello method is the homepath, for example bbc.com
#	return "I exist now!" 


#@app.route("/Elisabeth")
#def Elisabeth():
#	return "Elisabeth is here"
	
app.run(debug=True)

# control C stops the app from running 