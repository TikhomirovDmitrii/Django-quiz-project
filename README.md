# Quiz Project API

This is a Django-based API for managing quiz questions. It includes:
- RESTful endpoints using Django REST Framework
- Swagger/OpenAPI documentation
- Docker support for easy deployment

## Features
- Fetch random quiz questions via `/api/quiz/`
- Generate a specified number of questions using POST requests
- Swagger UI available at `/swagger/`

## Requirements
- Python 3.12+
- Django 4.2+
- MySQL database (for production)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<ваш-логин>/quiz_project.git
   cd quiz_project

2. Create a virtual environment and install dependencies:
python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
.venv\Scripts\activate     # Windows
pip install -r requirements.txt

3. Apply migrations and run the development server:
python manage.py migrate
python manage.py runserver

4. Open http://127.0.0.1:8000/swagger/ in your browser to access the API documentation.

## Docker Deployment
1. Build the Docker image:
docker build -t quiz_project .

2. Run the container:
docker run -p 8000:8000 quiz_project

