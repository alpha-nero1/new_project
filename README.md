# new_project

This project is a personal "capolavoro" or masterpiece in other words to which I gradualy implement new features and functionalities.

## Running the project.

1. Ensure python is installed on your machine
2. Once in the project directory run: `python manage.py runserver`

## Making database/model changes

1. run: `python manage.py makemigrations <app_name>`
2. run: `python manage.py migrate <app_name>`

... Note that with all above run with `python3` instead of `python` to run the python3 version.

## To remove old pyc files

1. run: `find . -name "*.pyc" -exec rm -f {} \;`
