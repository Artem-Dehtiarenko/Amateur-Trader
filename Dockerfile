# Use a base image with Python
FROM python:3.9-slim

# Install the necessary system dependencies (if needed)
RUN apt-get update && apt-get install -y \
git \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

# Install DVC
RUN pip install dvc

# Copy the entire project to the container
COPY . /app

# Go to the directory with the application
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt

# Command to run
CMD ["dvc", "repro"]