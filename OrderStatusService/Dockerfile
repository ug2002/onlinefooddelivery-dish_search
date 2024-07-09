# order-status-service/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY app.py .

# Specify the command to run on container start
CMD ["python", "app.py"]
