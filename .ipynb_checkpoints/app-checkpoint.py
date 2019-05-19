from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_dict_scrape

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

@app.route("/")
def home():

    mars_data = mongo.db.collection.find_one()

    return render_template("index.html", mars=mars_data)


@app.route("/scrape")
def scrape():

    mars_data = mars_dict_scrape.scrape_info()

#     mongo.db.collection.update({}, mars_data_dict, upsert=True)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)