# Use Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy all application files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 5000

# Command to run the Flask app
CMD ["python3", "main.py"]
