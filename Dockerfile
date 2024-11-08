FROM python:3.13.0-alpine3.20

RUN pip install django==5.1.3

CMD [ "sh" ] 
