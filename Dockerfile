# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run the unit tests first; if they fail, the build fails
RUN python run-tests.py

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]