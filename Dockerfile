# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the port on which the Flask app will run (change it if necessary)
EXPOSE 80

# Run the application
CMD ["python", "run.py"]
