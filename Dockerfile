FROM python:3.9-slim-buster

WORKDIR /app

COPY app/main.py .
COPY requirements.txt .
COPY app/dados_ecomerce.json .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]