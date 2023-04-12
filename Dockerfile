#Can not use python:3.11-alpine because of psycopg2 and other libraries

FROM python:3.11-slim-buster

# نصب pika به جای amqp
# RUN apt-get update && \
#     apt-get install -y \
#     gcc \
#     && \
#     rm -rf /var/lib/apt/lists/*

# install requirements for running project
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# copy project files to the container
COPY ./HotelCenter /app

# set the working directory to /app
WORKDIR /app

# create static folder
RUN mkdir -p static

# RUN sleep 10
# With this command we will test our project
# RUN python3 manage.py test