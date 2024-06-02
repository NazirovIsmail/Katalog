FROM  mirror.gcr.io/python:3.11-slim

#RUN apt update && apt install -y gcc

#install requirments
COPY requirements.txt /tmp/build/requirements.txt
RUN python -m pip install -r /tmp/build/requirements.txt

# install main application
# COPY README.md /tmp/build/README.md
# COPY pyproject.toml /tmp/build/pyproject.toml
COPY service /service
# RUN cd /service


ENTRYPOINT ["python", "/service/__main__.py"]