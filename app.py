from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_dict_scrape

app = Flask(__name__)

# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
# mongo = PyMongo(app)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")


@app.route("/")
def index():
    
    mars_data = mongo.db.collection.find_one()
    # If is a new instance and there is no mongoDB data, this will scrape before the initial load.
    try: 
        return render_template("index.html", mars_data=mars_data)

    except: 
        return redirect("/scrape",code=302)



@app.route("/scrape")
def scraper():
    
    mars_data = mars_dict_scrape.mars_data_dict()

    mongo.db.collection.update({}, mars_data, upsert=True)

    return redirect("/",code=302)

if __name__ == "__main__":
    app.run(debug=True)