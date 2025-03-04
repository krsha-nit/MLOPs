import pytest
import sqlite3
import requests
from CI.int_test_dbconn import create_user, get_user, get_weather, generate_user_weather_report

# Fixture for setting up a temporary database
@pytest.fixture
def setup_database(tmpdir):
    db_path = tmpdir.join("test.db")
    yield str(db_path)
    if db_path.exists():
        db_path.remove()

# Fixture for mocking the weather API
@pytest.fixture
def mock_weather_api(monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        if "city=London" in args[0]:
            return MockResponse({"temperature": 15, "conditions": "Cloudy"}, 200)
        else:
            return MockResponse(None, 404)

    monkeypatch.setattr(requests, "get", mock_get)

# Test database integration
def test_create_and_get_user(setup_database):
    db_path = setup_database

    # Create a user
    create_user(db_path, "john_doe", "john@example.com")

    # Retrieve the user's email
    email = get_user(db_path, "john_doe")

    # Assert the email is correct
    assert email == "john@example.com"

# Test API integration
def test_get_weather(mock_weather_api):
    # Test successful API call
    weather_data = get_weather("London")
    assert weather_data == {"temperature": 15, "conditions": "Cloudy"}

    # Test failed API call
    with pytest.raises(Exception):
        get_weather("InvalidCity")

# Test end-to-end report generation
def test_generate_user_weather_report(setup_database, mock_weather_api):
    db_path = setup_database

    # Create a user
    create_user(db_path, "john_doe", "john@example.com")

    # Generate a report
    report = generate_user_weather_report(db_path, "john_doe", "London")

    # Assert the report is correct
    assert report == {
        "username": "john_doe",
        "email": "john@example.com",
        "city": "London",
        "temperature": 15,
        "conditions": "Cloudy",
    }

    # Test user not found
    with pytest.raises(Exception):
        generate_user_weather_report(db_path, "invalid_user", "London")