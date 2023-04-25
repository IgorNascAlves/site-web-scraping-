FROM python:3.9-slim-buster

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8080

USER 1001

CMD ["uwsgi", "--chdir", "app/", "--http", "0.0.0.0:8080", "--master", "-p", "4", "-w", "wsgi:app"]