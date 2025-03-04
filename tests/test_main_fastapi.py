import pytest
from fastapi.testclient import TestClient
from CI.main_fastapi import app  # Assuming your FastAPI app is in main_fastapi.py

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "World"}

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "Pinged successful"}

def test_predict_approved():
    # Test case for an approved loan
    loan_data = {
        "Gender": "Male",
        "Married": "Yes",
        "Dependents": "1",
        "Education": "Graduate",
        "Self_Employed": "No",
        "ApplicantIncome": 6000,
        "CoapplicantIncome": 2000,
        "LoanAmount": 200000,
        "Loan_Amount_Term": 360,
        "Credit_History": 1.0,
        "Property_Area": "Semiurban"
    }
    response = client.post("/predict", json=loan_data)
    assert response.status_code == 200
    assert response.json() == {"loan_approval_status": "Approved"}

def test_predict_rejected():
    # Test case for a rejected loan
    loan_data = {
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
    response = client.post("/predict", json=loan_data)
    assert response.status_code == 200
    assert response.json() == {"loan_approval_status": "Rejected"}
    
def test_predict_dependents_3plus():
     # Test case for dependents as 3+
    loan_data = {
        "Gender": "Male",
        "Married": "Yes",
        "Dependents": "3+",
        "Education": "Graduate",
        "Self_Employed": "No",
        "ApplicantIncome": 7000,
        "CoapplicantIncome": 0,
        "LoanAmount": 150000,
        "Loan_Amount_Term": 360,
        "Credit_History": 1.0,
        "Property_Area": "Semiurban"
    }
    response = client.post("/predict", json=loan_data)
    assert response.status_code == 200
    assert response.json() == {"loan_approval_status": "Approved"}

def test_predict_invalid_input():
    # Test case with incomplete or invalid input
    loan_data = {
         "Gender": "Male",
        "Married": "Yes",
        "Dependents": "1",
        "Education": "Graduate",
        "Self_Employed": "No",
        "ApplicantIncome": 6000,
        "CoapplicantIncome": 2000,
        "LoanAmount": 200000,
        "Loan_Amount_Term": 360,
        "Credit_History": 1.0,
        
    }
    response = client.post("/predict", json=loan_data)
    assert response.status_code == 422
