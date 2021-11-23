FROM python:alpine3.7

COPY . /flaskapp
COPY ./requirements.txt /flaskapp/requirements.txt

WORKDIR /flaskapp

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]