import sqlite3
import requests

# Database operations
def create_user(db_path, username, email):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, email TEXT)")
    cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))
    conn.commit()
    conn.close()

def get_user(db_path, username):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT email FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# API operations
def get_weather(city):
    # Mock API URL (in real life, this would be a real API like OpenWeatherMap)
    url = f"https://mock-api.com/weather?city={city}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch weather data: {response.status_code}")

# Report generation
def generate_user_weather_report(db_path, username, city):
    email = get_user(db_path, username)
    if not email:
        raise Exception("User not found")

    weather_data = get_weather(city)
    if not weather_data:
        raise Exception("Failed to fetch weather data")

    report = {
        "username": username,
        "email": email,
        "city": city,
        "temperature": weather_data.get("temperature"),
        "conditions": weather_data.get("conditions"),
    }
    return report