# MLOPs Project

This project demonstrates the implementation of MLOPs using **Streamlit**, **Flask**, and **FastAPI**. Below are the instructions to set up and run the project locally or using Docker.

---

## **Table of Contents**
1. [Setup](#setup)
2. [Running the Applications](#running-the-applications)
   - [Streamlit](#streamlit)
   - [Flask](#flask)
   - [FastAPI](#fastapi)
3. [Docker Setup](#docker-setup)
4. [API Documentation](#api-documentation)

---

## **Setup**

### **1. Create a Virtual Environment**
Create and activate a virtual environment:

```bash
python -m venv venv
```

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### **2. Install Dependencies**
Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## **Running the Applications**

### **Streamlit**
Run the Streamlit app:

```bash
streamlit run {streamlit_file.py}
```

Replace `{streamlit_file.py}` with your Streamlit script filename.

---

### **Flask**
Run the Flask app:

```bash
flask --app flask_fastapi/main run --host=127.0.0.1 --port=5000 --debug
```

- Access at: `http://127.0.0.1:5000`
- Debug mode is enabled.

---

### **FastAPI**
Run the FastAPI app:

```bash
uvicorn flask_fastapi.main_fastapi:app --host 127.0.0.1 --port=8000 --reload
```

- Access at: `http://127.0.0.1:8000`
- Auto-reload is enabled for development.

---

## **Docker Setup**

### **1. Build the Docker Image**
Navigate to the project root folder (`MLOps`) and build the Docker image:

```bash
docker build -t flask-fastapi-api -f docker_containerization/Dockerfile .
```

### **2. Run the Docker Container**
Run the container with ports mapped for Flask (`5000`) and FastAPI (`8000`):

```bash
docker run -p 5000:5000 -p 8000:8000 flask-fastapi-api
```

- **Flask**: Access at `http://127.0.0.1:5000`
- **FastAPI**: Access at `http://127.0.0.1:8000`

---

## **API Documentation**

### **Swagger UI**
FastAPI automatically generates interactive API documentation. Access it at:

```
http://127.0.0.1:8000/docs
```

- View all routes and test endpoints directly.

---

### **ReDoc**
FastAPI also provides ReDoc documentation. Access it at:

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
- Replace `{streamlit_file.py}` with your Streamlit script filename.
- Use `--debug` for Flask and `--reload` for FastAPI during development.
- Ensure Docker Desktop is running when using Docker.
