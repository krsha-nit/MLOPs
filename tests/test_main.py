from CI.main import app
import json
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_ping(client):
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.data == b'Ping successful'
    
def test_predict(client):
    
    test_data = {
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
    }
    
    response = client.post("/predict", json=test_data)
    assert response.status_code == 200
    assert response.json=={"loan_approval_status": "Approved"}