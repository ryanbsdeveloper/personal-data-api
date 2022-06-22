FROM python:3.9

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# PARA DEPLOY HEROKU
# CMD uvicorn src.main:app --reload --host 0.0.0.0 --port $PORT
