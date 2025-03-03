Here’s a restructured and improved version of your `README.md` file. It is now more organized, easier to read, and includes clear sections for setup, running the applications, and accessing documentation.

---

# MLOPs Project

This project demonstrates the implementation of MLOPs using **Streamlit**, **Flask**, and **FastAPI**. Below are the instructions to set up and run the project.

---

## **Table of Contents**
1. [Setup](#setup)
2. [Running the Applications](#running-the-applications)
   - [Streamlit](#streamlit)
   - [Flask](#flask)
   - [FastAPI](#fastapi)
3. [API Documentation](#api-documentation)
   - [Swagger UI](#swagger-ui)
   - [ReDoc](#redoc)

---

## **Setup**

### **1. Create a Virtual Environment**
To isolate dependencies, create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### **2. Install Dependencies**
Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

---

## **Running the Applications**

### **Streamlit**
To run the Streamlit application, use the following command:

```bash
streamlit run {streamlit_file.py}
```

Replace `{streamlit_file.py}` with the actual filename of your Streamlit script.

---

### **Flask**
To run the Flask application, use the following command:

```bash
flask --app flask_fastapi/main run --host=127.0.0.1 --port=5000 --debug
```

- The application will be available at `http://127.0.0.1:5000`.
- Debug mode is enabled for easier development.

---

### **FastAPI**
To run the FastAPI application, use the following command:

```bash
uvicorn flask_fastapi.main_fastapi:app --host 127.0.0.1 --port 8000 --reload
```

- The application will be available at `http://127.0.0.1:8000`.
- The `--reload` flag enables auto-reloading during development.

---

## **API Documentation**

### **Swagger UI**
FastAPI automatically generates interactive API documentation using Swagger UI. Access it at:

```
http://127.0.0.1:8000/docs
```

- You can view all the defined routes.
- Send requests and see responses directly from the browser.

---

### **ReDoc**
FastAPI also provides ReDoc documentation, which is an alternative to Swagger UI. Access it at:

```
http://127.0.0.1:8000/redoc
```

---

## **Summary of Endpoints**

| Framework | URL                          | Description                     |
|-----------|------------------------------|---------------------------------|
| Flask     | `http://127.0.0.1:5000`      | Flask application               |
| FastAPI   | `http://127.0.0.1:8000`      | FastAPI application             |
| FastAPI   | `http://127.0.0.1:8000/docs` | Swagger UI for API documentation|
| FastAPI   | `http://127.0.0.1:8000/redoc`| ReDoc for API documentation     |

---

## **Notes**
- Ensure the virtual environment is activated before running any commands.
- Replace `{streamlit_file.py}` with the actual filename of your Streamlit script.
- Use `--debug` for Flask and `--reload` for FastAPI during development to enable auto-reloading.