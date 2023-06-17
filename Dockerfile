FROM python:3.9-slim-buster
WORKDIR /app
ENV PYTHONPATH="${PYTHONPATH}:/app"
RUN mkdir /app/app
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
COPY ./app /app/app
CMD uvicorn app.index:app --reload --host "0.0.0.0"
