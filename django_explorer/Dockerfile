FROM python:3.7-alpine

RUN mkdir -p /app/

WORKDIR /app

RUN pip install pipenv pip setuptools -U
RUN apk update && apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev

COPY ./Pipfile ./Pipfile

RUN pipenv install

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000/tcp

HEALTHCHECK --interval=6s --timeout=3s CMD wget --quiet --tries=1 --spider http://localhost:8000/ || exit 1

