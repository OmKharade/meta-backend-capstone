# Little Lemon Restaurant

![Lemon Web Application](restaurant\static\img\logo.png)

## Meta Backend Developer Capstone Project

![Meta](restaurant\static\img\meta.jpg)


This project is a web application for the Little Lemon restaurant, developed as the capstone project for the Meta Backend Developer course. It's built using Django and incorporates various features including menu management, table booking, and user authentication.

### Features

- **Home Page**: Displays an overview of the restaurant, including special offers and links to key sections.
- **Menu**: Shows the restaurant's menu items, which can be managed through the admin interface.
- **Table Booking**: Allows authenticated users to book tables at the restaurant.
- **User Authentication**: Implements token-based authentication for secure access to booking and menu management features.

### Technology Stack

- **Backend**: Django
- **API**: Django Rest Framework
- **Authentication**: Djoser and Token Authentication
- **Database**: MySQL

### Setup and Installation

1. Clone the repository:
``` shell
git clone https://github.com/OmKharade/meta-backend-capstone.git
cd meta-backend-capstone
```
2. Setup a virtual environment:
``` shell
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```
3. Install dependencies:
``` shell
pip install -r requirements.txt
```
4. Set up MySQL database:
    - Install MySQL if not already installed
    - Create a new MySQL database for the project
    - Update the DATABASES configuration in settings.py with your MySQL database details:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_database_name',
            'USER': 'your_mysql_username',
            'PASSWORD': 'your_mysql_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```
5. Run migrations:
``` shell
python manage.py migrate
```
6. Create a superuser:
``` shell
python manage.py createsuperuser
```
7. Run the development server:
``` shell
python manage.py runserver
```

### API Endpoints

- `/restaurant/menu/`: List all menu items or create a new one
- `/restaurant/menu/<int:pk>`: Retrieve, update or delete a menu item
- `/restaurant/booking/`: List all bookings or create a new one
- `/auth/`: Djoser authentication endpoints

### Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

### License

[MIT License](LICENSE)

### Acknowledgements

This project was completed as part of the Meta Backend Developer Specialization on Coursera.