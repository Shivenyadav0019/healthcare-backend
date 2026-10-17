# Healthcare Backend API

A healthcare backend application built using Python, Django REST Framework, and PostgreSQL.

## Features

- User registration and login
- JWT-based authentication
- Patient management APIs
- Doctor management APIs
- Patient-doctor assignment APIs
- User-specific patient access
- PostgreSQL database integration

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Simple JWT

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Login and obtain JWT tokens |
| POST | `/api/auth/refresh/` | Refresh access token |
| GET, POST | `/api/patients/` | List or create patients |
| GET, POST | `/api/doctors/` | List or create doctors |
| GET, POST | `/api/mappings/` | List or create doctor assignments |
| GET, DELETE | `/api/mappings/<patient_id>/` | View assignments or delete a mapping |

## Installation and Setup

### 1. Clone the Repository

Clone this repository from GitHub.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root and add your own database credentials:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your-database-password
DB_HOST=localhost
DB_PORT=5432
```

Do not upload your actual `.env` file to GitHub.

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## Authentication

Protected APIs use JWT authentication. Register an account and log in to obtain an access token.

Include the access token in the request header:

```text
Authorization: Bearer <access_token>
```

## Security

- Keep secret keys and database passwords private.
- Never commit real patient information or access tokens.
- Use dummy data for testing.
- Set `DEBUG=False` and configure production security before deployment.

## Author

Healthcare Backend API project developed using Django REST Framework and PostgreSQL.
