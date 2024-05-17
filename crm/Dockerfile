FROM python:3.11

WORKDIR /crm

COPY requirements.txt /crm

RUN pip install --no-cache-dir -r requirements.txt

COPY /crm /crm

EXPOSE 8000

CMD  ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]