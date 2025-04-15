from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [
        float(request.form["f1"]),
        float(request.form["f2"]),
        float(request.form["f3"]),
        float(request.form["f4"])
    ]
    prediction = model.predict([features])
    return render_template("index.html", prediction=int(prediction[0]))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
