#import necessary libraries
from flask import Flask, render_template

#create instance of Flask app
app = Flask(__name__)

#create route that renders index.html template
@app.route("/")
def index():
    movie_list = ["Avengers", "End Game", "Sky Falls", "Batman", "Squid Game"]
    return render_template("index.html", list=movie_list)

if __name__ == "__main__":
    app.run(debug=True)