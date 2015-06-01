# No Ball Django application server

FROM python:3.4.3-wheezy

MAINTAINER Shinichi Nakagawa <spirits.is.my.rader@gmail.com>

# add to application
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD ./noball /app/
RUN mkdir /app/noball/deploy
RUN python manage.py collectstatic --noinput

# run application
EXPOSE 8000
EXPOSE 3306
