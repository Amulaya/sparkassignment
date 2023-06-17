FROM python:3.9-slim-buster
WORKDIR /app
ENV PYTHONPATH="${PYTHONPATH}:/app"
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./app /app
CMD uvicorn index:app --reload --host "0.0.0.0"
