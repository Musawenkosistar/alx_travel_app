# ALX Travel App

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=white)

A robust travel listing platform built with Django and Django REST Framework. The application allows users to browse and book travel accommodations, leave reviews, and manage listings as hosts.

## ✨ Features

- 🔌 **RESTful API** with Django REST Framework
- 🗄️ **MySQL Database** for reliable, scalable data storage
- 📄 **Swagger/OpenAPI** documentation for interactive API exploration
- 🌐 **CORS Support** for frontend-backend communication
- 🔐 **Environment Variables** for secure configuration
- ⚙️ **Celery Integration** for asynchronous background tasks (e.g., emails, cleanup)

## Prerequisites

- Python 3.8+
- MySQL 5.7+
- Redis or RabbitMQ (for Celery tasks)

## Installation

1. **Clone the repository**
```bash
 git clone https://github.com/heba-webdev/alx_travel_app_0x00.git
   cd alx_travel_app_0x00
```

2. **Set up virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

- Create a .env file in the project root

- Add your configuration (see example below)

```bash
Example .env file:
DEBUG=True
SECRET_KEY=your-secret-key-here
DB_NAME=alx_travel_db
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=3306
```

5. **Set up database**
   
- Create a MySQL database

- Update the .env file with your database credentials

7. **Run migrations**
```bash
python manage.py migrate
```

### Running the Application

```bash
celery -A alx_travel_app_0x00 worker -l info
```

## Project Structure

```bash
alx_travel_app/
├── alx_travel_app/            # Project settings and configurations
│   ├── settings.py            # Django settings
│   ├── urls.py                # Root URL configuration
│   └── ...
├── listings/                  # Travel listing and booking app
│   ├── migrations/            # DB migrations
│   ├── models.py              # Models: Listing, Booking, Review
│   ├── views.py               # API views
│   ├── serializers.py         # DRF serializers
│   └── urls.py                # App URL routing
├── users/                     # Custom User model and related logic
│   └── ...
├── .env                       # Environment config
├── requirements.txt           # Python dependencies
└── manage.py                  # Django CLI
```
