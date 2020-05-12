# Aenshtyns Blog

### Live site

[Personal-Blog](https://aenshtyns-blog.herokuapp.com/)


#### Built by

[Mohamed Abdullahi](https://github.com/aenshtyn)

## Description

This is a Flask application that is built as a blog. There are two types of users. 1. The writers and 2. The readers. Writers can create posts and upload them to the blog, they also have the ability to delete unneccessary comments from the Readers. Readers can go trhough the posts, comment on any of them, and even subscribe to recieve notification of new posts.

## User Story

As a user, I would like to view the blog posts on the site
As a user, I would like to comment on blog posts
As a user, I would like to view the most recent posts
As a user, I would like to an email alert when a new post is made by joining a subscription.
As a user, I would like to see random quotes on the site
As a writer, I would like to sign in to the blog.
As a writer, I would also like to create a blog from the application.
As a writer, I would like to delete comments that I find insulting or degrading.
As a writer, I would like to update or delete blogs I have created.

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all blogs, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with blogs that have been posted by writes and be able to subscribe to the blog|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|
|Subscription | **Email Address**| Flash message "Succesfully subsbribed to D-Blog"|


## Setup/Installation Requirements

* python3.7
* pip
* virtualenv

## Cloning
* In your terminal:

  $ git clone https://github.com/aenshtyn/Personal-Blog/

  $ cd Personal-Blog

## Running the Application
* Creating the virtual environment

        $ python3.7 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ python3.7 -m pip install Flask
        $ python3.7 -m pip install Flask-Bootstrap
        $ python3.7 -m pip install Flask-Script

* To run the application, in your terminal:

        python3.7 manage.py server

## Testing the Application

* To run the tests for the class files:

        $ python3.7 manage.py tests

## Technologies Used

* Python3.6
* Virtualenv
* Flask
* HTML
* Bootsrap & CSS
* Git Version Control
* Postgresql
* Heruko

## Support and contact details

If you have any issues or questions you can contact me at demahom93@gmail.com

###### LICENSE

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
