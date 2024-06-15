FROM python:3.12.4-slim

COPY ./src .

RUN apt update && apt upgrade -y
RUN pip install -r requirements.txt


CMD ["python", "main.py"]