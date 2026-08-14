# Use a minimal base image with Python 3.9 installed
FROM python:3.9-slim

# Set the working directory to /app/backend
WORKDIR /app/backend

# Copy the entire backend_files contents into /app/backend_files
# This creates the exact directory structure your relative path (../backend_files/) requires
COPY . /app/backend_files/

# Copy the actual Python application code to our working directory
COPY . .

# Install Python dependencies listed in requirements.txt
RUN pip3 install -r requirements.txt

# Define the command to run the Streamlit app on port 8501 and make it accessible externally
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableXsrfProtection=false"]

# NOTE: Disable XSRF protection for easier external access in order to make batch predictions
