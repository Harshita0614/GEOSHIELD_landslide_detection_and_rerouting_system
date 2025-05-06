'''@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Received data:", data)

        # Force high-risk prediction for testing
        return jsonify({'prediction': 1})  # Always high risk for testing

    except Exception as e:
        print("Error in /predict:", str(e))
        return jsonify({'error': str(e)}), 500
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
        return jsonify({'error': str(e)}), 500'''
