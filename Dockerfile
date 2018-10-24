FROM python:3.6.6

RUN pip install flask

COPY src/ src
CMD python src/server.py

