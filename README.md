# Overview

This is a shell of a commerce website made with Django and Python. This is my first Django project and I am trying to learn how Django works to set up simple websites.

To start the webpage on your computer, type **python manage.py runserver**. To view the webpage, in your browser type **localhost:8000** 

I would like to expand the functionality of this site to sell dice I make to keep creater costs lower.

[Software Demo Video](https://youtu.be/xSvXEFWVUfk)

# Web Pages

**Home**
The navagation bar at the top is linked on all pages. The top three Dice and Image models are sent to the page to be shown.

**Shop**
This page dynamically shows all of the dice. If you click on a set it will take you to the individual page for that set. 

**Individual Sets**
These pages are loaded dynamically by using the primary key for that set of dice. 

**About**
This page just tells a little about how dice are made.

# Development Environment

This was written using VSCode, using Django and Python.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Get Started With Django](https://realpython.com/get-started-with-django-1/)
* [Activating Virtual Environment using Windows](https://stackoverflow.com/questions/55142774/how-to-activate-virtual-environment-in-django)
* [How to link to static files](https://docs.djangoproject.com/en/4.1/howto/static-files/)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Click on images to enlarge them
* Cart functionality
* User functionality
* Hook up shopping app
