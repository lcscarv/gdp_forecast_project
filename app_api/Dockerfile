FROM python:3.8.10

WORKDIR /app/src

RUN apt-get update && apt-get upgrade -y

COPY ./app_api/requirements.txt /app/src/requirements.txt

RUN pip install -r requirements.txt

ADD ./app_api /app/src

# Give access to run the run.sh script.
RUN chmod +x run.sh

CMD ["bash", "./run.sh"]