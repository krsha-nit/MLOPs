# Use the official Python image
FROM python:3.11.9-bookworm

# Set the working directory
WORKDIR /docker_flask_fastapi

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Copy the application files
COPY docker_containerization .

# Install dependencies
RUN pip3 install -r requirements.txt

# Expose ports for Flask and FastAPI
EXPOSE 5000 8000

# Command to run both Flask and FastAPI
## CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
CMD ["sh", "-c", "flask --app main run --host=0.0.0.0 --port=5000 --debug & uvicorn main_fastapi:app --host 0.0.0.0 --port 8000 --reload"]