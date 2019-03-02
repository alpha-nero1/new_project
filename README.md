# new_project

This project is a personal "capolavoro" or masterpiece in other words to which I gradualy implement new features and functionalities.

The project stack is Python/Django/SQLite3, the documentation for Django can be found here: https://docs.djangoproject.com/en/2.1/

## Running the project.

1. Ensure python is installed on your machine

### Mac

2. Once in the project directory run: `python manage.py runserver`

### Windows

2. Once in the project directory run: `py manage.py runserver`

## Making database/model changes

1. run: `python manage.py makemigrations <app_name>`
2. run: `python manage.py migrate <app_name>`

... Note that with all above run with `python3` instead of `python` to run the python3 version.

## To remove old pyc files

1. run: `find . -name "*.pyc" -exec rm -f {} \;`

## Model Layer

Django provides an abstraction layer (the “models”) for structuring and manipulating the data of your Web application.

## View Layer

Django has the concept of “views” to encapsulate the logic responsible for processing a user’s request and for returning the response.

## Template Layer

The template layer provides a designer-friendly syntax for rendering the information to be presented to the user.

## Forms
