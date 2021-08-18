FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

#Make a directory for app
WORKDIR /app


ENV EG_DATABASE_URL="postgresql://root:root@localhost:32700/emoticon_generator"
ENV ES_URL="http://localhost:5431"
RUN export SECRET_KEY=$(openssl rand -hex 32)

RUN apt-get update

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /app .

CMD ["python", "main.py"]