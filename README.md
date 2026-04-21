# RotinaVillas – Django Web Application

## Project Overview

RotinaVillas is a full-stack Django web application for browsing and booking villas.  
The platform supports user authentication, villa management, bookings, reviews, RESTful APIs, and asynchronous background processing.

This project was developed as part of the Django Advanced Course @ SoftUni and demonstrates best practices in Django architecture, REST API design, and deployment.

---

## Live Demo

https://rotinavillas.onrender.com

---

## Tech Stack

Backend:
- Django 5
- Django REST Framework

Database:
- PostgreSQL

Async Processing:
- Celery
- Redis

Deployment:
- Render
- Gunicorn
- WhiteNoise

Frontend:
- Django Templates
- Bootstrap

---

## Authentication and Users

- Custom user model (AppUser) extending AbstractUser
- Features:
  - Registration
  - Login / Logout
  - Profile management

User Groups:
- Regular Users
- Moderators (extended permissions)

---

## Project Structure

The project is modular and consists of multiple Django apps:

- accounts – user management  
- villas – villa listings  
- bookings – booking system  
- reviews – user reviews  
- common – shared logic and mixins  
- api – REST API endpoints  

---

## Database Design

- Multiple models with:
  - One-to-Many relationships (User → Bookings)
  - Many-to-Many relationships (Users ↔ Villas)
- Model-level validations and clean architecture

---

## Features

Villas:
- Browse all villas
- View villa details
- Filter and sort listings

Bookings:
- Create bookings (authenticated users only)
- Prevent overlapping reservations
- Edit/Delete bookings (owner or moderator)

Reviews:
- Users can leave reviews after completed bookings
- Conditional logic based on booking dates

---

## Email Confirmation

After a successful booking:

- A confirmation email is sent to the user
- Implemented using Django's send_mail

Development:
- Console email backend

Production:
- SMTP configurable (e.g. Gmail, ABV)

---

## Asynchronous Processing (Celery)

Celery is used for background task execution.

Implemented tasks:
- Booking confirmation email
- Scheduled deletion of old bookings

Stack:
- Celery worker
- Redis as broker

Note:
On free hosting environments, tasks may run synchronously if a worker is not deployed.

---

## REST API

The project includes RESTful endpoints using Django REST Framework.

Features:
- Serializers
- API Views
- Permissions (IsAuthenticatedOrReadOnly)

Example endpoints:
- /api/villas/
- /api/bookings/

---

## Frontend and Templates

- 17+ dynamic pages
- Template inheritance with base layout
- Responsive design using Bootstrap
- Custom template tags and filters
- Fully connected navigation

---

## Security

- CSRF protection
- XSS protection via Django templates
- Environment variables for sensitive data
- No hardcoded credentials

---

## Static and Media Handling

- Static files served via WhiteNoise
- Proper separation:
  - static/ → source files
  - staticfiles/ → generated during deployment

---

## Testing

- Unit tests for models, views, and user functionality
- Minimum 20+ tests included

---

## Environment Variables

Example .env configuration:

SECRET_KEY=your_secret_key
DEBUG=True

DATABASE_URL=postgres://user:password@host:port/db

REDIS_URL=redis://localhost:6379/0

EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email
EMAIL_HOST_PASSWORD=your_password
EMAIL_USE_TLS=True

---

## Deployment (Render)

Steps:

1. Create PostgreSQL service
2. Set environment variables
3. Configure build command:

pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate

4. Start command:

gunicorn RotinaVillas.wsgi

---

## Local Setup

git clone <repo-url>
cd RotinaVillas

python -m venv venv
source venv/bin/activate  (Linux/Mac)
venv\Scripts\activate     (Windows)

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver

---

## Key Concepts Demonstrated

- Class-Based Views (CBVs)
- Custom User Model
- Forms and Validation
- REST API design
- Background tasks with Celery
- Modular architecture
- Deployment and environment configuration

---

## Notes

- Static files must be placed in static/, not staticfiles/
- collectstatic is required in production
- Large media files should be optimized

---

## License

This project is for educational purposes as part of the Django Advanced course.