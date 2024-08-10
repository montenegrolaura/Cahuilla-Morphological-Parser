FROM python:3.9

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r /app/web/requirements.txt

ENV PYTHONPATH /app

EXPOSE 5000

#CMD tail -f /dev/null
CMD ["python", "/app/web/app.py"]