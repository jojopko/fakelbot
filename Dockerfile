FROM python:3.9.16-bullseye

WORKDIR /webapp

COPY . /webapp

RUN ["pip", "install", "-r", "req.txt"]

CMD ["sh", "-c", "gunicorn -w 4 -k gevent -b 0.0.0.0:${SERVER_PORT} 'fakel:app'"]

