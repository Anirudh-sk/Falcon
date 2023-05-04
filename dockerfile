# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN apt-get update
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y
RUN python -m pip install pipwin
RUN python -m pipwin install pyaudio
RUN python -m pip install pyaudio

# Install any needed packages specified in requirements.txt
RUN python -m pip install -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "main.py"]

# docker tag local-image:tagname new-repo:tagname
# docker push new-repo:tagname
# docker push anirudh30/falcon:tagname

