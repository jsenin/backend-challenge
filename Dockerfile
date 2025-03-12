FROM python:3-slim AS base
# base stuff here

FROM base AS development

WORKDIR /src

COPY pyproject.toml .

RUN pip install -e .

EXPOSE 8000

CMD ["fastapi", "run", "app/main.py", "--port", "8000", "--reload"]

FROM base AS production

WORKDIR /src

COPY . .

RUN pip install .

EXPOSE 8000

CMD ["fastapi", "run", "app/main.py", "--port", "8000", "--reload"]
