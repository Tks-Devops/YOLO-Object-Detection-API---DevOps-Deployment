FROM python:3.8-slim

# Install system dependencies required for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*  # Cleanup to reduce image size

# Set working directory
WORKDIR /app

# Copy application files including YOLO weights and config
COPY app.py requirements.txt yolov3.cfg yolov3.weights devops.jpg /app/

# Install required Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (if needed)
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]

