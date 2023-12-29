# backend_project/containers/Dockerfile

FROM python:3.10

# GDAL installation
RUN apt-get update && apt-get install -y python3-gdal

# Set the working directory
WORKDIR /backend

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY backend /backend

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
