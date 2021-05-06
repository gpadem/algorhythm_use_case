from flask import Flask, jsonify, render_template
from flask import request

from bs4 import BeautifulSoup
import requests

import torch
from transformers import pipeline


def get_book_url:

#----------FLASK-----------------------------#

@app.route("/")
def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)

@app.route("/summarize", methods=["GET", "POST"])
def book_page():
    if request.method == "GET":
        return render_template("book.html")
    else:
        form_book = request.form["Link to the book from Gutenberg Project"]

    

    output = round(prediction[0], 2)

    return render_template(
        "index.html", prediction_text="Churn rate $ {}".format(output)
    )


@app.route("/results", methods=["POST"])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True, port=5000)