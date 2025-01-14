# Use Python 3.10 image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt first and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

# Expose port
EXPOSE 5000

# Run the application
#CMD ["python", "app.py"]
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]