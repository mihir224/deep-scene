from flask import Flask, render_template, request, jsonify
from model import Meso4
from PIL import Image
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
model = Meso4()
model.load('./model_weights.h5')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img = Image.open(file).resize((256, 256))
        img = np.array(img) / 255.0
        prediction = model.predict(np.expand_dims(img, axis=0))[0][0]
        result = "Real" if prediction > 0.5 else "Deepfake"
        response = {
            "result": result,
            "predicted_class": prediction.item()
        }
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=4200)
