# Collage

Collage is a project for collecting and displaying images with location metadata.

## Installation

Collage is unready for production. To test it, install the requirements, and perform the following installation steps.

### Requirements


### Install Steps

1. Link collage_nginx.conf to nginx sites available
2. Install and configure your choice of database and configure it in collage/settings.py
3. manage.py migrate
4. Run with `$ uwsgi collage_uwsgi.ini`

## TODO:

+ Create templating
+ Add support for user login and upload
+ Support for maps
+ Use a makefile for easy installation
