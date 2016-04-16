FROM ubuntu:latest
MAINTAINER Felipe Amarante "felipeamarante@gmail.com"
EXPOSE 5000
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
