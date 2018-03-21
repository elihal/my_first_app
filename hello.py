from flask import Flask, render_template

#import <-- you can also use this istead of from ..

app = Flask("MyApp") #importing an app that's called "MyApp"

#roots is the relative path of the website, i.e. what's after the /

@app.route("/") #decorator .. before you do this code, do this other code
def hello():
	#hello method is the homepath, for example bbc.com
	return "Hello you! " 

#app.run(debug=True)

#app.run starts your application - otherwise it's not run
#without app.run it is waiting for interaction from visitors on the webpage

#copy link that the terminal gives you or put localhost:5000
@app.route("/idontexist") #decorator .. before you do this code, do this other code
def idontexist():
	#hello method is the homepath, for example bbc.com
	return "I exist now!" 


@app.route("/Elisabeth")
def Elisabeth():
	return "Elisabeth is here"
	
app.run(debug=True)

# control C stopps the app from running 