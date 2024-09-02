# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Create a non-root user and set the home directory
RUN useradd -m myuser

# Set the working directory in the container
WORKDIR /usr/src

# Copy the requirements file into the container
COPY requirements.txt ./

# Switch to the non-root user
USER myuser

# Install the required packages
RUN pip install -r requirements.txt

# Copy the rest of your application code into the container
#COPY --chown=myuser:myuser src/ .

# Expose the port the app runs on
EXPOSE 3011

# Command to run the application
CMD ["python", "app.py"]

