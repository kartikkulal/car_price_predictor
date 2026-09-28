# 🚗 Car Price Prediction

A Machine Learning web application that predicts the **resale price of a used car** based on details such as company, car name, year, kilometers driven, fuel type, and other relevant features.

## 📌 Project Overview

The project uses a Machine Learning regression model to estimate the selling price of a used car.

The trained model is integrated with a **Flask web application**, allowing users to enter car details through a web interface and get an estimated price instantly.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Flask
* HTML
* CSS
* Jupyter Notebook
* Git & GitHub

## 🤖 Machine Learning

The project follows these steps:

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Categorical Encoding
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Model Pipeline Creation
10. Model Deployment using Flask

A **Scikit-learn Pipeline** is used to handle preprocessing and prediction consistently.

## 📊 Input Features

The application takes information such as:

* Car Name
* Company
* Manufacturing Year
* Kilometers Driven
* Fuel Type
* Seller Type
* Transmission
* Owner Details

## 🌐 Web Application

The Flask application provides a simple interface where users can enter the car details.

After submitting the form, the trained Machine Learning model processes the input and predicts the estimated resale price.

## 📁 Project Structure

```text
Car-Price-Prediction/
│
├── app.py
├── model.pkl
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── notebooks/
│   └── car_price_prediction.ipynb
├── requirements.txt
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/car-price-prediction.git
```

Navigate to the project directory:

```bash
cd car-price-prediction
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000/
```

## 🔮 Prediction

Enter the required car information and click **Predict Price**.

The application will return the estimated price of the car.

## 🎯 Future Improvements

* Improve model accuracy with additional features
* Try different regression algorithms
* Add model performance comparison
* Improve UI/UX
* Deploy the application on a cloud platform
* Add more car brands and updated market data

## 👨‍💻 Author

**Kartik Kulal**

Computer Science and Engineering
BMS College of Engineering
