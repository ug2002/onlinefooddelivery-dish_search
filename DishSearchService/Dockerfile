# DishSearchService Dockerfile

# Use the official Python image.
FROM python:3.11-slim

# Set the working directory in the container.
WORKDIR /app

# Copy the requirements file into the container.
COPY requirements.txt .

# Install dependencies.
RUN pip install -r requirements.txt

# Copy the rest of the application files.
COPY app.py .
COPY dishes.txt .

# Expose the port the app runs on.
EXPOSE 5000

# Define the command to run the app.
CMD ["python", "app.py"]
