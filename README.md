
# JikoTrack: A Web-Based Solution for Small Restaurant Management

## Overview

JikoTrack is a comprehensive web-based solution designed to streamline inventory management for small eateries. This platform integrates essential restaurant management functions into a single system, enhancing operational efficiency, financial transparency, and sustainability.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Methodology](#methodology)
- [Installation](#installation)
  - [Cloning the Project](#cloning-the-project)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [System Requirements](#system-requirements)
- [Contributing](#contributing)
- [License](#license)
- [Contributors](#contributors)

## Introduction

Small restaurants often face significant challenges with inventory management, leading to operational inefficiencies and financial discrepancies. JikoTrack addresses these issues by providing an integrated platform that combines advanced inventory and accounting modules. This system is designed to help restaurant owners monitor inventory levels in real-time, manage finances effectively, and allocate resources efficiently.

## Features

- **Inventory Management**: Track inventory levels in real-time, manage stock movements, and streamline supplier communications.
- **Accounting Module**: Simplify expense tracking, revenue management, and financial reporting for improved financial transparency.
- **Reporting Dashboard**: Visualize key performance indicators and gain actionable insights into business operations.
- **User-Friendly Interface**: Intuitive navigation ensures ease of use for small restaurant owners and employees.
- **Scalability**: Suitable for small and medium-sized restaurants.
- **Cross-platform Support**: Backend development in Python (Django) and frontend development in JavaScript (Nuxt3).

## Methodology

- **Structured System Analysis and Design Methodology (SSADM)**: Employed for deep analysis and structured planning of the system.
- **Design Thinking**: Utilized for problem-solving, emphasizing user-centric solutions and rapid prototyping.

## Installation

### Cloning the Project

Clone the repository using the following link:

```bash
git clone https://github.com/Gambi204/fullstackErpSystem.git
cd fullstackErpSystem
```

### Backend Setup

1. **Create a virtual environment**:

    ```bash
    python -m venv venv
    ```

2. **Activate the virtual environment**:
    - On Windows:
      ```bash
      .\venv\Scripts\Activate
      ```
    - On Unix or MacOS:
      ```bash
      source venv/bin/activate
      ```

3. **Install the required Python packages**:

    ```bash
    pip install mysqlclient django-mysql django-cors-headers PyJWT django-filter markdown djangorestframework phonenumbers djangorestframework-simplejwt pycountry
    ```

4. **Install Pipenv**:

    ```bash
    pip install pipenv
    ```

5. **Configure the database**:
    - Open `settings.py` and configure the credentials in the `DATABASES` section to connect to your database.

6. **Set up and migrate your database**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. **Run the Django Development Server**:

    ```bash
    python manage.py runserver
    ```

### Frontend Setup

1. **Navigate to the frontend directory**:

    ```bash
    cd frontend
    ```

2. **Install the required packages**:

    ```bash
    npm install
    ```

3. **Run the development server**:

    ```bash
    npm run dev
    ```

## Project Structure

```plaintext
fullstackErpSystem/
│
├── backend/
│   ├── venv/                     # Virtual environment
│   ├── manage.py                 # Django management script
│   ├── requirements.txt          # Required Python packages
│   ├── Pipfile                   # Pipenv configuration file
│   ├── Pipfile.lock              # Pipenv lock file
│   ├── project_name/             # Django project directory
│   │   ├── __init__.py
│   │   ├── settings.py           # Django settings
│   │   ├── urls.py               # URL declarations
│   │   ├── wsgi.py               # WSGI configuration
│   │   ├── asgi.py               # ASGI configuration
│   ├── app_name/                 # Example app directory
│   │   ├── migrations/           # Database migrations
│   │   │   ├── __init__.py
│   │   ├── __init__.py
│   │   ├── admin.py              # Admin definitions
│   │   ├── apps.py               # App configuration
│   │   ├── models.py             # Data models
│   │   ├── tests.py              # Tests
│   │   ├── views.py              # Views
│   │   ├── serializers.py        # DRF serializers
│   │   ├── urls.py               # App URLs
│
├── frontend/
│   ├── node_modules/             # Node.js modules
│   ├── .nuxt/                    # Nuxt build directory
│   ├── assets/                   # Uncompiled assets such as SASS, LESS, or JavaScript
│   ├── components/               # Vue.js components
│   ├── layouts/                  # Layouts for Nuxt
│   ├── pages/                    # Nuxt pages
│   ├── plugins/                  # Plugins for Nuxt
│   ├── static/                   # Static files
│   ├── store/                    # Vuex store
│   ├── nuxt.config.js            # Nuxt configuration file
│   ├── package.json              # NPM package configuration
│   ├── package-lock.json         # NPM package lock file
│
├── .gitignore                    # Git ignore file
├── README.md                     # Project README file
```

## Usage

After completing the installation steps, you can start using JikoTrack by accessing the development servers for both the backend and frontend. The web-based interface will allow you to manage your restaurant's inventory and accounting needs efficiently.

## Dependencies

- **Frameworks**:
  - [Django](https://www.djangoproject.com/)
  - [Django REST Framework](https://www.django-rest-framework.org/)
  - [Nuxt3](https://nuxt.com/)
- **Python Packages**:
  - [mysqlclient](https://pypi.org/project/mysqlclient/)
  - [django-mysql](https://pypi.org/project/django-mysql/)
  - [django-cors-headers](https://pypi.org/project/django-cors-headers/)
  - [PyJWT](https://pypi.org/project/PyJWT/)
  - [django-filter](https://pypi.org/project/django-filter/)
  - [markdown](https://pypi.org/project/Markdown/)
  - [djangorestframework](https://pypi.org/project/djangorestframework/)
  - [phonenumbers](https://pypi.org/project/phonenumbers/)
  - [djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/)
  - [pycountry](https://pypi.org/project/pycountry/)

## System Requirements

- **Backend**:
  - [Python 3.8+](https://www.python.org/downloads/)
  - [Django](https://www.djangoproject.com/)
  - [MySQL](https://dev.mysql.com/downloads/)

- **Frontend**:
  - [Node.js](https://nodejs.org/)
  - [Nuxt3](https://nuxt.com/)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code follows the project's coding standards and includes appropriate tests.

## License

MIT License

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Contributors

Strathmore University
