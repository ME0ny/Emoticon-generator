FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

#Make a directory for app
WORKDIR /app

RUN export SECRET_KEY=$(openssl rand -hex 32)

RUN apt-get update

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /app .

CMD ["python", "main.py"]