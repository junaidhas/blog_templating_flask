from flask import Flask, render_template # Flask is a python framework to build web applications
import requests # a python library to extract API's



app = Flask(__name__) # creating a new flask object

NPOINT_data = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

@app.route('/') #home url
def get_blog():
    return render_template("post.html",posts = NPOINT_data)

@app.route('/post/<int:id_num>') # read more url
def read_blog(id_num):
    print(id_num)
    return render_template("index.html",posts = NPOINT_data, ID = id_num)

if __name__ == "__main__": # run the flask application in debug mode
    app.run(debug=True)
