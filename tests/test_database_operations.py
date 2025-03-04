# test_database_operations.py
import pytest
import os
from CI.database_operations import create_user, get_user

@pytest.fixture
def setup_database(tmpdir):
    db_path = os.path.join(tmpdir, "test.db")
    yield db_path
    if os.path.exists(db_path):
        os.remove(db_path)

def test_create_and_get_user(setup_database):
    db_path = setup_database

    # Create a user
    create_user(db_path, "john_doe", "john@example.com")

    # Retrieve the user's email
    email = get_user(db_path, "john_doe")

    # Assert the email is correct
    assert email == "john@example.com"