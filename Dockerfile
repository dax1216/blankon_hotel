# pull official base image
FROM docker.io/python:3.12.2-slim-bookworm AS python

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/root/.local/bin:${PATH}"

RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg dependencies
  libpq-dev

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# copy entrypoint
COPY ./entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start


# copy project
COPY . /app

EXPOSE 8000

# run entrypoint
CMD ["/start"]
