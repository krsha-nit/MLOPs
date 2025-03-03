from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model
with open("classifier.pkl", "rb") as model_pickle:
    clf = pickle.load(model_pickle)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ping", methods=["GET"])
def ping():
    return "Ping successful, flask"

@app.route("/predict", methods=["POST"])
def prediction():
    """
    Returns loan application status using ML model
    """
    # Get JSON data from the request
    loan_req = request.get_json()
    print(loan_req)

    # Convert categorical variables to numerical
    input_data = {
        "Gender": 1 if loan_req["Gender"] == "Male" else 0,
        "Married": 1 if loan_req["Married"] == "Yes" else 0,
        "Dependents": int(loan_req["Dependents"].replace("3+", "3")),
        "Education": 1 if loan_req["Education"] == "Graduate" else 0,
        "Self_Employed": 1 if loan_req["Self_Employed"] == "Yes" else 0,
        "ApplicantIncome": loan_req["ApplicantIncome"],
        "CoapplicantIncome": loan_req["CoapplicantIncome"],
        "LoanAmount": loan_req["LoanAmount"],
        "Loan_Amount_Term": loan_req["Loan_Amount_Term"],
        "Credit_History": loan_req["Credit_History"],
        "Property_Area": loan_req["Property_Area"],
    }

    # Create TotalIncome feature
    input_data["TotalIncome"] = input_data["ApplicantIncome"] + input_data["CoapplicantIncome"]

    # One-hot encode Property_Area
    property_area = input_data["Property_Area"]
    input_data["Property_Area_Semiurban"] = 1 if property_area == "Semiurban" else 0
    input_data["Property_Area_Urban"] = 1 if property_area == "Urban" else 0

    # Drop unnecessary fields
    input_data.pop("ApplicantIncome")
    input_data.pop("CoapplicantIncome")
    input_data.pop("Property_Area")

    # Create a DataFrame from the input data
    input_df = pd.DataFrame([input_data])

    # Ensure the input DataFrame has the same columns as the training data
    if hasattr(clf, "feature_names_in_"):
        # Reorder columns to match the model's training data
        input_df = input_df.reindex(columns=clf.feature_names_in_, fill_value=0)

    # Make prediction
    result = clf.predict(input_df)

    # Map prediction to approval status
    pred = "Approved" if result[0] == 1 else "Rejected"

    return jsonify({"loan_approval_status": pred})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
    
    
"""
sample test data: -- will get "rejected" as output
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{
    "Gender": "Male",
    "Married": "Yes",
    "Dependents": "0",
    "Education": "Graduate",
    "Self_Employed": "No",
    "ApplicantIncome": 50000,
    "CoapplicantIncome": 0,
    "LoanAmount": 500000,
    "Loan_Amount_Term": 360,
    "Credit_History": 1.0,
    "Property_Area": "Urban"
}'

_________________________
{
    "Gender": "Male",
    "Married": "No",
    "Dependents": "0",
    "Education": "Graduate",
    "Self_Employed": "No",
    "ApplicantIncome": 50000,
    "CoapplicantIncome": 0,
    "LoanAmount": 500000,
    "Loan_Amount_Term": 360,
    "Credit_History": 1.0,
    "Property_Area": "Urban"
}
"""