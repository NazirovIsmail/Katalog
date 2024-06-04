FROM  mirror.gcr.io/python:3.11-slim

#install requirments
COPY requirements.txt /tmp/build/requirements.txt
RUN python -m pip install -r /tmp/build/requirements.txt

COPY service /service


ENTRYPOINT ["python", "/service/__main__.py"]