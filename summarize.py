from flask import Flask, jsonify, render_template
from flask import request


app = Flask(__name__)



@app.route("/book_summary")
def read_BOOK(data):

    article = data.split(". ")
    sentences = []
    for sentence in article:
        review = regex.sub("[^A-Za-z0-9]",' ', sentence)
        sentences.append(review.replace("[^a-zA-Z]", " ").split(" "))        
    sentences.pop()     
    return sentences


@app.route("/multiply", methods=["GET", "POST"])
def multiply_page():
    if request.method == "GET":
        return render_template("multiply.html")

    else:
        form_First = request.form["First number"]
        form_Second = request.form["Second number"]
        multiplication = int(form_First) * int(form_Second)
        return str(multiplication)


@app.route("/projects")
def projects_page():
    return render_template("projects.html")


if __name__ == "__main__":
    app.run(debug=True)