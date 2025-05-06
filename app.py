from flask import Flask, request, jsonify, render_template
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load(r"E:\Capstone_project_25\geoshield_landslide_model_selected.pkl")  # Adjust path as needed

# Home route to render the frontend
@app.route('/')
def home():
    return render_template('index.html')  # Assumes index.html is in the templates/ folder

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Received data:", data)

        # Extract the 7 required features
        features = [
            data['longitude'],
            data['latitude'],
            data['precipitation'],
            data['wind_speed'],
            data['location_accuracy'],
            data['event_time'],
            data['event_weekday']
        ]

        # Make prediction
        prediction = model.predict([features])
        print("Prediction result:", prediction)

        return jsonify({'prediction': int(prediction[0])})

    except Exception as e:
        print("Error in /predict:", str(e))
        return jsonify({'error': str(e)}), 500
# Run the server
if __name__ == '__main__':
    app.run(debug=True)