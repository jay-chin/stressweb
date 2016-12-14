FROM ubuntu:latest

RUN apt-get -y update

# Install Python
RUN apt-get install -y python-dev python-pip

# Install stress
RUN apt-get install stress

# Create webapp directory
ADD stressweb/. /webapp

# Add requirements
ADD requirements.txt /webapp

# Install uwsgi and requirements
RUN pip install uwsgi
RUN pip install -r /webapp/requirements.txt

ENV HOME /webapp
WORKDIR /webapp

EXPOSE 8000

ENTRYPOINT ["uwsgi", "--http", "0.0.0.0:8000", "--module", "app:app", "--processes", "1", "--threads", "8"]
