
FROM python:3.9.15-slim-bullseye

WORKDIR /home/jovyan/work
ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/work"

RUN apt-get update && apt-get install -y git

ADD ../requirements.txt /home/jovyan/work/requirements.txt
RUN pip install -r requirements.txt
