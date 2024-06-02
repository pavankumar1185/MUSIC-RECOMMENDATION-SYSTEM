from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import random
import csv

result = []

with open("predictions.csv", mode="r") as file:
    csvFile = csv.reader(file)
    next(csvFile, None)
    for lines in csvFile:
        # print(lines)
        result.append(lines[1])


app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
# print("result", result)
model = None


@app.route("/", methods=["GET"])
def index():
    return render_template("index2.html")


@app.route("/recommend", methods=["GET"])
def get_recommendations():
    data = request.args
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    # artist = data.get("artist")
    genre = data.get("genre")
    area = data.get("area")

    if not genre or not area:
        return jsonify({"error": "Please provide artist, genre, and area"}), 400

    res = random.sample(result, 5)

    try:
        # Call the model's recommendation function with the provided parameters
        recommendations = model.get_recommendations(genre, area)
        return jsonify(recommendations)
    except Exception as e:
        return jsonify({"result": res})


if __name__ == "__main__":
    app.run(debug=True)
