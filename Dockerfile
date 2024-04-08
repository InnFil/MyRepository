FROM python:3.11

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY /app /app

COPY ./app/.env /app
# ENV SECRET_KEY=django-insecure-2yw(9v&a&%kb!ycjkyb3zgdga46u82dem(4$ig*cg)qstv87wk
# ENV DEBUG=True

EXPOSE 8000

CMD  ["python3", "manage.py", "runserver", "0.0.0.0:8000"]