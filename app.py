from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the model and vectorizer
model = joblib.load("category_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    description = request.form['description']
    X = vectorizer.transform([description])
    category = model.predict(X)[0]
    return render_template("index.html", prediction=category, description=description)

if __name__ == "__main__":
    app.run(debug=True)