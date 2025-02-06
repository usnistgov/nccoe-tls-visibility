
FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt
COPY certs/DigiCertCA.crt.pem  /usr/local/share/ca-certificates/DigiCertCA.crt.pem

EXPOSE 5000

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN update-ca-certificates
RUN pip install --no-cache-dir pip-system-certs
