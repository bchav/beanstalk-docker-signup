FROM alpine:3.3
RUN apk add --no-cache bash git nginx uwsgi uwsgi-python py-pip \
       	&& pip install --upgrade pip \
       	&& pip install flask redis gunicorn
COPY templates/ /templates/
COPY app.py /app.py
EXPOSE 5000
CMD [ "gunicorn", "app:app", "-b", "0.0.0.0:5000" ]
