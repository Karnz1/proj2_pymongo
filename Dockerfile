# Use the official Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY app.py .

RUN mkdir ./templates

COPY ./templates ./templates

EXPOSE 8006

# Set the command to run the application
CMD ["python", "app.py"]