from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd
import uvicorn

# Define the input data model using Pydantic
class LoanApplication(BaseModel):
    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: str

# Initialize FastAPI app
app = FastAPI()

# testing hello world!
@app.get("/")
def read_root():
    return {"message": "World"}

# testing /ping
@app.get("/ping")
def ping():
    return {"message": "Pinged successful"}



# Load the pre-trained model
with open("CI/classifier.pkl", "rb") as f:
    clf = pickle.load(f)

# Predict endpoint
@app.post("/predict")
def predict(loan_req: LoanApplication):
    # Convert input data to a dictionary
    input_data = loan_req.dict()

    # Convert categorical variables to numerical
    input_data['Gender'] = 1 if input_data['Gender'] == "Male" else 0
    input_data['Married'] = 1 if input_data['Married'] == "Yes" else 0
    input_data['Education'] = 1 if input_data['Education'] == "Graduate" else 0
    input_data['Self_Employed'] = 1 if input_data['Self_Employed'] == "Yes" else 0
    input_data['Dependents'] = int(input_data['Dependents'].replace('3+', '3'))

    # Create TotalIncome feature
    input_data['TotalIncome'] = input_data['ApplicantIncome'] + input_data['CoapplicantIncome']

    # One-hot encode Property_Area
    property_area = input_data['Property_Area']
    input_data['Property_Area_Semiurban'] = 1 if property_area == "Semiurban" else 0
    input_data['Property_Area_Urban'] = 1 if property_area == "Urban" else 0

    # Drop unnecessary fields
    input_data.pop('ApplicantIncome')
    input_data.pop('CoapplicantIncome')
    input_data.pop('Property_Area')

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

    return {"loan_approval_status": pred}

# Run the FastAPI app using uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
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