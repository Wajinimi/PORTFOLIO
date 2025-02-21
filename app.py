from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app)

# Load the machine learning model if it exists
if os.path.exists('model.pkl'):
    model = joblib.load('model.pkl')
else:
    model = None
    print("Warning: No model.pkl found - using mock predictions")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    if model:
        # Use the machine learning model's prediction
        prediction = model.predict([[data['Number_of_Bedrooms'],
                                     data['Number_of_Bathrooms'], 
                                     data['House_Age'], data['Location_Score'], 
                                     data['Garage_Size'], data['Nearby_Schools_Rating'], 
                                     data['Proximity_to_City_Center'], data['Square_Feet']]])[0]
    else:
        # Use a mock prediction if the model is not available
        prediction = 123456  # Example mock prediction value
    
    return jsonify({'predictedPrice': prediction, 'rawOutput': data})

if __name__ == '__main__':
    app.run(debug=True)


    