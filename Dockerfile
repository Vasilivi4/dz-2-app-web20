FROM python:3.11-slim

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY pyproject.toml $APP_HOME/pyproject.toml
COPY poetry.lock $APP_HOME/poetry.lock

COPY requirements.txt $APP_HOME/requirements.txt

RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --only main

COPY . .

EXPOSE 3000

CMD ["python", "app.py"]