# Use an official Python image as a base
FROM python:3.9-slim

# Set environment variables to prevent Python from buffering outputs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements files into the container
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the Gradio default port
EXPOSE 7860

# Define the entry point for the container
CMD ["python", "app/main.py"]
