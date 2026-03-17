# RotinaVillas

RotinaVillas is a simple Django web application for browsing and booking vacation villas.  
The idea of the project is to simulate a small villa rental platform where users can view available villas, make bookings and leave reviews.

This project was created as part of the **Django Basics course at Software University (SoftUni).**

---

## Project Overview

The goal of the project is to practice the main concepts of Django:

- Working with models and database relationships
- Creating forms with validation
- Using Class-Based Views and Function-Based Views
- Implementing CRUD operations
- Working with Django templates and template inheritance
- Building a structured Django project with multiple apps

The application allows users to browse villas, view detailed information, make bookings and leave reviews.

---

## Features

### Villas
- Browse all available villas
- View detailed information about a villa
- Create a new villa listing
- Edit existing villas
- Delete villas

### Bookings
- Create a booking for a villa
- Prevent overlapping bookings
- Edit an existing booking
- Delete bookings
- View all bookings

### Reviews
- Leave reviews for villas
- Give ratings from 1 to 5
- See reviews left by other users
- Calculate average rating for each villa

### Other functionality
- Custom template filters
- Custom 404 error page
- Responsive layout using Bootstrap
- PostgreSQL database

---

## Project Structure

The project is organized into several Django apps:


RotinaVillas/
│
├── common/
│ pages like Home, About and Contacts
│
├── villas/
│ villa model, forms and views
│
├── bookings/
│ booking functionality
│
├── reviews/
│ review system for villas
│
├── templates/
│ HTML templates for all pages
│
├── static/
│ CSS files and other static resources
│
└── RotinaVillas/
main project configuration




---

## Technologies Used

The project is built with:

- Python
- Django
- PostgreSQL
- HTML
- CSS
- Bootstrap 5

---

## Installation

Follow these steps to run the project locally.

### 1. Clone the repository
## Installation

Follow these steps to run the project locally.

### 1. Clone the repository


git clone https://github.com/lpkotsev/RotinaVillas_DjangoProject

cd rotinavillas


### 2. Create virtual environment


python -m venv venv


Activate it:

Windows


venv\Scripts\activate


Mac / Linux


source venv/bin/activate


### 3. Install dependencies


pip install -r requirements.txt


### 4. Configure database

Update the database settings in:


RotinaVillas/settings.py


Example configuration:


DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'rotinavillas_db',
'USER': 'postgres',
'PASSWORD': 'postgres',
'HOST': 'localhost',
'PORT': '5432',
}
}


### 5. Apply migrations


python manage.py migrate


### 6. Start the development server


python manage.py runserver


Open the application in your browser:


http://127.0.0.1:8000/


---

## How to Use the Application

After starting the server you can:

- Browse all available villas
- View details about each villa
- Create your own villa listing
- Make bookings for specific dates
- Leave reviews and ratings

Navigation links are available in the top menu for all main pages.

---

## Future Improvements

Some possible improvements for the project:

- Add user authentication
- Add villa image uploads
- Improve search and filtering
- Add pagination for large lists

---

## Author

Project created by Lachezar Kotsev
