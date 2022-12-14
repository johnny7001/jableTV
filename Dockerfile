# FROM python:3.9
FROM python:slim 
WORKDIR /app


COPY jable_api.py /app

COPY requirements.txt .

RUN pip install -r requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "/app/jable_api.py"]
EXPOSE 3123

