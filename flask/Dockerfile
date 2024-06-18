FROM python:3

WORKDIR /usr/src/app

RUN pip install Flask

COPY server.py .

EXPOSE 5000

CMD ["python", "server.py"]

