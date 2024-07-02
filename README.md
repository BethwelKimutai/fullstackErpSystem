
# JikoTrack: A Web-Based Solution for Small Restaurant Management

## Overview

JikoTrack is a comprehensive web-based solution designed to streamline accounting and inventory management for small eateries. This platform integrates essential restaurant management functions into a single system, enhancing operational efficiency, financial transparency, and sustainability.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Methodology](#methodology)
- [Installation](#installation)
  - [Cloning the Project](#cloning-the-project)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [System Requirements](#system-requirements)
- [Contributing](#contributing)
- [License](#license)
- [Contributors](#contributors)

## Introduction

Small restaurants often face significant challenges with accounting and inventory management, leading to operational inefficiencies and financial discrepancies. JikoTrack addresses these issues by providing an integrated platform that combines advanced inventory and accounting modules. This system is designed to help restaurant owners monitor inventory levels in real-time, manage finances effectively, and allocate resources efficiently.

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
git clone https://github.com/BethwelKimutai/fullstackErpSystem.git
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

## Usage

After completing the installation steps, you can start using JikoTrack by accessing the development servers for both the backend and frontend. The web-based interface will allow you to manage your restaurant's inventory and accounting needs efficiently.

## Dependencies

- **Frameworks**:
  - Django
  - Django REST Framework
  - Nuxt3
- **Python Packages**:
  - mysqlclient
  - django-mysql
  - django-cors-headers
  - PyJWT
  - django-filter
  - markdown
  - djangorestframework
  - phonenumbers
  - djangorestframework-simplejwt
  - pycountry

## System Requirements

- **Backend**:
  - Python 3.8+
  - Django
  - MySQL

- **Frontend**:
  - Node.js
  - Nuxt3

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code follows the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License.

## Contributors

Strathmore University
