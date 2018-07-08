FROM jazzdd/alpine-flask:python3

ADD requirements.txt /tmp_ins/
RUN pip install -r /tmp_ins/requirements.txt
RUN rm -rf /tmp_ins/

ADD app.py /app/
ADD streifen/ /app/streifen/
ADD templates/ /app/templates/
