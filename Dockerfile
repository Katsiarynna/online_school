FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /eduplatform
COPY poetry.lock pyproject.toml /eduplatform/
RUN pip install -U pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install
COPY . ./
COPY ../.env ./.env
EXPOSE 8000
ENTRYPOINT ["bash", "-c", "/eduplatform/entrypoint.sh"]
