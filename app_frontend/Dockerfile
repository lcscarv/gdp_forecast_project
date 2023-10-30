FROM python:3.8.10

WORKDIR /app/src

RUN apt-get update && apt-get upgrade -y

COPY ./app_frontend/requirements.txt /app/src/requirements.txt

RUN pip install -r requirements.txt

ADD ./app_frontend /app/src

CMD ["streamlit", "run", "frontend/main.py", "--server.port", "8501"]