from flask import Flask, jsonify, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('model.joblib')

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    # Assuming the model's get_recommendations function takes input parameters
    data = request.json  # Get the data sent in the POST request
    artist = data.get('artist')  # Get the artist name from the request
    genre = data.get('genre')  # Get the genre from the request
    area = data.get('area')  # Get the area from the request
    
    # Call the model's recommendation function with the provided parameters
    recommendations = model.get_recommendations(artist, genre, area)
    
    # Assuming the model returns recommendations in a suitable format
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
