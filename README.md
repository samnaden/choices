# choices
As E-40 once said: "Everybody got choices." What will you choose?

## Running Locally
- create a python virtual env, 3.10 <= python_version < 3.13
- activate virtual env
- run the below
  - ```commandline
    pip install poetry==2.1.3
    poetry config virtualenvs.create false
    poetry install
    pre-commit install
    ```
- `docker-compose down -v`
- `docker-compose up -d`
- `export DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/choices && alembic upgrade head`
- `export PYTHONPATH=. && export DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/choices && python3 ./app/db/seed/local_dummy.py`
- `export DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/choices && poetry run uvicorn app.main:app --reload`

## APPLICATION TODO
- Use a cookie to track user session (or at least something else besides passing name along the flow).
- Add a cleanup job to remove visitors and their questions that are over a day old.
- Add a location element to show questions to visitors ranked by proximity.

## INFRA TODO
- Get this deployed somewhere.
- Once deployment to a cloud vendor has been proved out, use GH actions to accomplish it.
