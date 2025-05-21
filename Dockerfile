# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "streamlit_app/app.py"]
