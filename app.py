from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__)

model = pickle.load(open("LinearRegressionModel.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html",predictions=None)


@app.route("/predict", methods=["POST"])
def predict():
    name = request.form["name"].strip()
    company = request.form["company"].strip()
    year = int(request.form["year"])
    kms_driven = int(request.form["kms_driven"])
    fuel_type = request.form["fuel_type"].strip()

    input_data = pd.DataFrame({
    "name": [name],
    "company": [company],
    "year": [year],
    "kms_driven": [kms_driven],
    "fuel_type": [fuel_type]
})
    
    # Your model's expected input format
    prediction = model.predict(input_data)[0]

    return render_template(
        "index.html",
        prediction=float(prediction)
    )


if __name__ == "__main__":
    app.run(debug=True)