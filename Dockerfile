FROM python:3.8.5-slim

RUN apt-get update && apt-get upgrade -y
RUN apt-get install apt-utils -y
RUN apt-get install python3 python3-dev default-libmysqlclient-dev build-essential -y

WORKDIR /app
COPY . ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN pip install gunicorn mysqlclient

RUN mkdir /images

VOLUME [ "/images" ]

EXPOSE 8000

RUN chmod 777 boot.sh

ENTRYPOINT [ "./boot.sh" ]