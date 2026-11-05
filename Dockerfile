FROM python3.11-slim

WORKDIR /app

COPY . .

CMD ["python", "runner.py"]