from flask import Flask, render_template, request

app = Flask(__name__)

def simple_ckd_predict(age, blood_pressure, albumin, sugar, serum_creatinine):
    # Placeholder logic: Replace with your trained model
    # Very basic rule-based for demonstration
    if albumin > 3 or serum_creatinine > 1.5:
        return "High Risk of CKD"
    else:
        return "Low Risk of CKD"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    blood_pressure = float(request.form['blood_pressure'])
    albumin = float(request.form['albumin'])
    sugar = float(request.form['sugar'])
    serum_creatinine = float(request.form['serum_creatinine'])

    result = simple_ckd_predict(age, blood_pressure, albumin, sugar, serum_creatinine)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)