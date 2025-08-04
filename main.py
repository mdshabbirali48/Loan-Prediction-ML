from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('loan_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = [
        int(request.form['Gender']),
        int(request.form['Married']),
        int(request.form['Dependents']),
        int(request.form['Education']),
        int(request.form['Self_Employed']),

        float(request.form['ApplicantIncome']),
        float(request.form['CoapplicantIncome']),
        float(request.form['LoanAmount']),
        float(request.form['Loan_Amount_Term']),
        float(request.form['Credit_History']),
        int(request.form['Property_Area'])
    ]
    
    prediction = model.predict([np.array(data)])
    result = 'Approved' if prediction[0] == 1 else 'Rejected'
    return render_template('index.html', prediction_text=f'Loan {result}')

if __name__ == '__main__':
    app.run(debug=True)
