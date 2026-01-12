FROM python:3.10-slim

WORKDIR /app

COPY data_usage.py .

CMD ["python", "data_usage.py"]
