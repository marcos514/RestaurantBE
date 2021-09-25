FROM python:3.9.7
RUN mkdir /app/
COPY . /app/api
RUN pip install --upgrade pip && pip install -r /app/api/requirements.txt
WORKDIR /app/api
CMD ["supervisord", "-n", "-c","/app/api/supervisor/supervisord.conf"]