FROM python:3.9-slim

# Set the working directory to /app/backend
WORKDIR /app/backend

# Copy the entire backend_files contents into /app/backend_files
# This creates the exact directory structure your relative path (../backend_files/) requires
COPY . /app/backend_files/

# Copy the actual Python application code to our working directory
COPY . .

# Install dependencies from the requirements file
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Define the command to start the application using Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:7860", "app:superkart_api"]
