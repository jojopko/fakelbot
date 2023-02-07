FROM python:3.9.16-bullseye

WORKDIR /webapp

COPY . /webapp

RUN ["pip", "install", "-r", "req.txt"]

CMD ["python3", "web.py"]

