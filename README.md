# Django App - Index Lab Beatles

## Description
A media company wants to build a dashboard to give more detail on The Beatles' top songs.
Authenticated users can post new songs to the database.
The company has provided a CSV file with the top songs from The Beatles.

## Project
Project is built with Django and Python.
Rest API is built with Django Rest Framework.
Design is based on vertical sliced architecture. 
More info: https://garywoodfine.com/implementing-vertical-slice-architecture/

## Installation

First clone the git repo `git clone git@github.com:Piwero/index-lab-beatles.git`

Move inside the new repo `cd index-lab-beatles/`

Create a virtualenv `virtualenv -p python3 .venv`

Activate your virtualenv `source .venv/bin/activate`

Create your secrets file with a django secret key `echo "SECRET_KEY=-yd@)1^bgoyddwnzax6i*hthd@vc@=(+3(n%@(t)y(rj4(61ua)" > .env`

Install dependencies for project in environment  `poetry install` (if this fails, you may need to delete the file poetry.lock and try `poetry install` again)

Run migrations `python manage.py migrate`

Import data to DB `python manage.py import_csv_songs_to_db "songs/files/task_data.csv"`

Create user `python manage.py createsuperuser`

## Run server

With `source .venv/bin/activate`

You can run `python manage.py runserver`

## Run tests
`pytest .`

