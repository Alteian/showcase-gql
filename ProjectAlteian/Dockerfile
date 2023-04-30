FROM python:3.11.1-buster

RUN mkdir /code

RUN python -m pip install --upgrade pip

RUN pip install gunicorn

COPY requirements.txt ./

RUN python3 -m pip install -r requirements.txt

COPY ./ /code/

WORKDIR /code
