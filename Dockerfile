FROM python:3.7.2-slim-stretch

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt

CMD ["python3", "run.py"]