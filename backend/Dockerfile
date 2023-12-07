FROM python:3.10
LABEL authors="gecko"

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /app/backend
COPY . /app/backend


EXPOSE 8000
ENTRYPOINT ["/bin/bash", "start_app.sh"]