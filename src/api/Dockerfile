FROM python:latest

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY . /api
WORKDIR /api
RUN python setup.py install
RUN rm -rf /api

RUN pip freeze | grep server
RUN which python3.6

COPY ./main.py /usr/local/server/main.py
WORKDIR /usr/local/server

ENV WEB_PORT 80

CMD /usr/local/bin/gunicorn -w 4 -b :$WEB_PORT main:app