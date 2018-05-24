FROM jazzdd/alpine-flask:python3

ADD app.py /app/
ADD requirements.txt /app/
ADD streifen/ /app/streifen/
ADD swagger /app/swagger/
