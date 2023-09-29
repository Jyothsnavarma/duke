

#Use an official Python runtime as a parent image

FROM python:3.8-slim

 

#Set the working directory in the container

WORKDIR /one-one_pro

 

#Copy the current directory contents into the container at /app

COPY server.py /one-one_pro

COPY config.json /one-one_pro

 

#Install any needed packages specified in requirements.txt

# If you have a requirements.txt file for dependencies

 

EXPOSE 8888

#Define the command to run your application

CMD ["python", "server.py"]
