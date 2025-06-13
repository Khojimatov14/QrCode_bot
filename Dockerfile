FROM python:3.12-slim

WORKDIR /AnyQrCodeBot

RUN apt-get update && apt-get install -y \
    libjpeg-dev zlib1g-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "app.py"]
