# URL Shortener

## Overview

This project is a Django-based URL shortening service. It allows users to create shortened versions of URLs, which can then be easily shared or embedded in various contexts.

## Features

- **URL Shortening**: Shorten long URLs into more manageable links.
- **Redirection**: Automatically redirect users to the original URL when accessing the shortened link.
- **Admin Panel**: Manage and monitor the shortened URLs through Django's built-in admin interface.

## Project Structure

- **shortener**: Contains the core logic for URL shortening and redirection.
- **static**: Static assets like CSS, JavaScript, and images.
- **templates**: HTML templates used for rendering the web pages.
- **urlShortener**: Django app responsible for handling URL shortening.
- **.gitignore**: Specifies which files and directories should be ignored by Git.
- **Procfile**: Configuration for deploying the app to Heroku.
- **README.md**: This document, providing an overview of the project.
- **manage.py**: Command-line utility for interacting with the Django project.
- **requirements.txt**: List of dependencies required to run the project.
- **runtime.txt**: Specifies the Python version used in the project.

## Installation

1. **Clone the repository**:
   - git clone https://github.com/yourusername/url-shortener.git
   - cd url-shortener
2. **Create a virtual environment**:
- python3 -m venv env
- source env/bin/activate  # On Windows use `env\Scripts\activate`
3. **Install dependencies**:
- pip install -r requirements.txt
4. **Set up the database**:
- python manage.py migrate
5. **Run the development server**:
- python manage.py runserver

## Deployment
- The project is configured for deployment on Heroku. The Procfile and runtime.txt files ensure that the app is deployed with the correct settings and Python version.

## Contributing
- Contributions are welcome! Please create a new branch and open a pull request with your changes.
