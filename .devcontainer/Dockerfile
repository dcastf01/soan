
FROM python:3.9.15-slim-bullseye

WORKDIR /home/jovyan/work
ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/work"

ADD ../requirements.txt /home/jovyan/work/requirements.txt
RUN pip install -r requirements.txt
