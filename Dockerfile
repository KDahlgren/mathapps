# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /mathapps

# Copy the current directory contents into the container at /app
ADD . /mathapps

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run app.py when the container launches
CMD [ "python", "./apps/mypi/src/mypi.py", "2" ]
