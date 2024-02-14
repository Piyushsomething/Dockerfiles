# Use the official Python image as a base image
FROM python:3.9 AS build

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY backend/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the remaining files to the container
COPY backend/ .

# Expose port 8888 (the port FastAPI will run on)
EXPOSE 8888

# Start FastAPI using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888", "--proxy-headers"]


