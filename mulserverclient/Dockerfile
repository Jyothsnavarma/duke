

#Use an official Python runtime as a parent image

FROM python:3.8-slim

 

#Set the working directory in the container

WORKDIR /one-many_pro

 

#Copy the current directory contents into the container at /app

COPY mulserver1.py /one-many_pro

COPY mulserver2.py /one-many_pro

COPY mulconfig.json /one-many_pro

 

#Install any needed packages specified in requirements.txt

# If you have a requirements.txt file for dependencies

 

 

#Expose the ports for both servers

EXPOSE 9964

EXPOSE 9901
