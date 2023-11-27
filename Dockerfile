FROM python:3.9

RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /app

COPY ./req.txt .

RUN pip install -r req.txt

COPY ./referal ./referal

CMD ["python3", "./referal/manage.py","runserver", "0.0.0.0:8000"]

