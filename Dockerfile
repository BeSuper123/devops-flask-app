FROM python:3.14

WORKDIR /usr/src/app

COPY . .

RUN pip install flask

EXPOSE 5000

RUN chmod +x lab1.sh && ./lab1.sh

ENTRYPOINT ["flask", "--app", "hello", "run", "--host=0.0.0.0"]
