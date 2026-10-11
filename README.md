# Inventory Management API

A RESTful Inventory Management API built with **FastAPI, SQLAlchemy, and PostgreSQL**. It supports product creation, retrieval, searching, updating, and deletion.

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Database:** PostgreSQL
- **Validation:** Pydantic
- **Testing:** Pytest
- **Environment Management:** uv

## Features

- Create new products
- Retrieve a product by ID
- List all products
- Search products by name
- Update existing products
- Delete products
- Automatic table creation using SQLAlchemy
- Automated tests using a separate SQLite test database

## Project Structure

```text
invertory-api/
├── main.py
├── models.py
├── schemas.py
├── database.py
├── crud.py
├── tests/
│   ├── conftest.py
│   └── test_items.py
├── .env
├── .gitignore
├── pyproject.toml
└── README.md
```

## Setup

### 1. Install dependencies

Install [uv](https://docs.astral.sh/uv/) if it isn't already installed, then run:

```bash
uv sync
```

### 2. Configure PostgreSQL

Create a PostgreSQL database named `inventory`.

Create a `.env` file in the project root:

```env
POSTGRESQL_DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/inventory
```

Replace `YOUR_PASSWORD` with your PostgreSQL password.

### 3. Run the API

```bash
uv run uvicorn main:app --reload
```

### 4. Explore the API

Open the interactive Swagger documentation:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/products/` | Create a product |
| GET | `/products/` | List all products |
| GET | `/products/search?product_name=laptop` | Search products by name |
| GET | `/products/{product_id}` | Retrieve a product by ID |
| PUT | `/products/{product_id}` | Update a product |
| DELETE | `/products/{product_id}` | Delete a product |

## Example Request

Create a product using `POST /products/`:

```json
{
  "product_name": "Laptop",
  "category": "Electronics",
  "quantity": 10,
  "price": 45000
}
```

## Run Tests

```bash
uv run pytest -v
```

The automated tests use a separate temporary SQLite database, keeping test data isolated from the PostgreSQL development database.

## Security

- Store database credentials in `.env`.
- Never commit `.env` or real database credentials to GitHub.
- Use `.gitignore` to exclude environment files and local database files.

## Future Improvements

- Authentication and authorization
- Pagination for product listings
- Database migrations using Alembic
- Docker support
- CI/CD with GitHub Actions

## Database Migrations with Alembic

This project uses Alembic to manage PostgreSQL database schema changes.

### Setup

Install the project dependencies:

```bash
uv sync
```

Configure your PostgreSQL connection in the `.env` file:

```env
POSTGRESQL_DATABASE_URL=your_postgresql_connection_url
```

### Running Migrations

Check the current migration revision:

```bash
uv run alembic current
```

Generate a migration after changing a SQLAlchemy model:

```bash
uv run alembic revision --autogenerate -m "describe your change"
```

Review the generated migration script before applying it.

Apply migrations:

```bash
uv run alembic upgrade head
```

Roll back one migration:

```bash
uv run alembic downgrade -1
```

**Note:** Review migration scripts before applying or reversing them. Downgrading can cause data loss if a migration removes columns or tables.