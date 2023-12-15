FROM python:3.10-slim
WORKDIR /django_tree_menu

ENV POETRY_VERSION=1.5.1 \
    PATH="/root/.local/bin:$PATH" \
    PYTHONPATH="/django_tree_menu"

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    curl build-essential postgresql-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml ./

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    poetry config virtualenvs.create false  && \
    poetry install

COPY init-script.sh /init-script.sh

RUN chmod +x /init-script.sh
ENTRYPOINT ["/init-script.sh"]

COPY src/ ./src/

CMD ["python3", "src/manage.py", "runserver", "0.0.0.0:8000"]
