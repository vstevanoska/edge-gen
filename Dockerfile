FROM python:3

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y fluidsynth ffmpeg sox

VOLUME /app
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .