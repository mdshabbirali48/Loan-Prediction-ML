# Loan-Prediction-ML


# Loan Approval Prediction Web App
 
This is a Simple Machine Learning web application I built to predict whether a loan should be approved based on user inputs. It's designed for beginners and intermediates to understand how a real-world ML model is built, trained, and deployed using Flask.

---

## Project Goal

The main aim of this project is to:
- Train a classification model on loan applicant data
- Predict loan approval based on certain features
- Deploy it using a Flask interface

---

## ML Model Details

I used a **Logistic Regression** model here because:
- The output is binary (Approved/Not Approved)
- It's simple, interpretable, and works well for a starter-level classification task

> Trained using scikit-learn and saved as a `.pkl` file for deployment.

---

## Project Structure

Loan-Prediction-ML/
│
├── app.py # Flask backend
├── loan_model.pkl # Trained ML model
├── loan_data.csv # Dataset 
├── templates/
│ └── index.html # Frontend form UI
├── static/ # (Optional) CSS/JS files
└── README.md # This file



