# engageHRMS

Welcome to engageHRMS, a comprehensive Human Resource Management System built using Django. This project is designed to streamline HR processes, providing an efficient, secure, and insightful platform for managing all aspects of human resources.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Applications](#applications)
  - [Core](#core)
  - [Employee Management](#employee-management)
  - [Attendance](#attendance)
  - [Payroll](#payroll)
  - [Performance](#performance)
  - [Recruitment](#recruitment)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

engageHRMS is an all-in-one solution for managing human resources within an organization. It encompasses various functionalities such as employee management, attendance tracking, payroll processing, performance evaluation, and recruitment management. This system is designed to be user-friendly and scalable, suitable for organizations of all sizes.

## Features

- **Employee Management:** Comprehensive management of employee details and records.
- **Attendance Tracking:** Automated attendance tracking and reporting.
- **Event Hnadling:** Efficient corporate event management with automated scheduling.

## Applications

### Accounts
The Core application serves as the backbone of the engageHRMS system. It includes the essential functionalities and configurations required for the system to operate smoothly. This application manages:
- User authentication and authorization.
- Dashboard and navigation.
- System settings and configurations.

The Employee Management application handles all aspects related to employee information. Key features include:
- Adding, editing, and deleting employee records.
- Managing employee personal details, job titles, and departments.
- Document management (e.g., contracts, ID proofs).
- Employee self-service portal for updating personal information.

### Calendar
Handles events scheduling and management, employee leaves and sick off days. Features include:
- Event creation.
- Leave management (sick leave, vacation, etc.).
- Attendance reports and summaries.


## Installation

To install and set up engageHRMS, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/opiyo24/engageHRMS.git
   cd engageHRMS
   ```

2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

7. **Access the application:**
   Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- **Admin Interface:** Access the Django admin interface at `http://127.0.0.1:8000/admin/` using the superuser credentials to manage the system.
- **Employee Portal:** Employees can log in and access their portal to view and update personal information.
- **HR Dashboard:** HR personnel can manage employees, track attendance and handle company events.

## Contributing

The developer welcomes contributions from the community. To contribute to engageHRMS, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a new Pull Request.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.


---

Thank you for using engageHRMS! If you have any questions or need further assistance, please feel free to reach out.