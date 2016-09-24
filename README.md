# uPyApp - Micro-service template for python

## Features

## Structure

## How to use

copy the project, search for `MyApp` and `my-app` and change it to whatever you like

## Setup and run

to init the project

```
cp example/my-app.ini my-app.ini
cp example/uwsgi.ini uwsgi.ini 
virtualenv --system-site-packages virtualenv
source bin/activate
pip install -r requirements.txt
```

you can script `uwsgi.ini` edits with crudini

```
crudini --set uwsgi.ini uwsgi cheaper-rss-limit-soft "$(( TOTAL_MEM * 1 / 3 ))"
crudini --set uwsgi.ini uwsgi cheaper-rss-limit-hard "$(( TOTAL_MEM * 3 / 8 ))"
```
