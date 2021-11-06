FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY const.py .
COPY uwsgi.ini .

CMD ["uwsgi", "uwsgi.ini"]
#CMD [ "python", "./const.py" ]

