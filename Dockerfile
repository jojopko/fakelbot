FROM python:3.9.16-bullseye

WORKDIR /webapp

COPY . /webapp

RUN ["pip", "install", "-r", "req.txt"]

CMD ["sh", "-c", "gunicorn --log-level debug -w 2 -k gevent -b ${SERVER_HOST}:${SERVER_PORT} 'fakel:app'"]

