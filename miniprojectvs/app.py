from flask import Flask, request, jsonify
import numpy as np
from sklearn.linear_model import LinearRegression

# Initialize Flask app
app = Flask(__name__)

# Dummy ML model
# Let's assume we trained this with past weather data
X_train = np.array([[20], [25], [30], [35], [40]])  # Example temperatures
y_train = np.array([0, 0, 1, 1, 1])  # 0: No rain, 1: Rain
model = LinearRegression().fit(X_train, y_train)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    temperature = data.get('temperature')
    if temperature is None:
        return jsonify({'error': 'Temperature is required'}), 400

    # Make prediction
    prediction = model.predict([[temperature]])
    result = 'Rain' if prediction[0] > 0.5 else 'No Rain'

    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
