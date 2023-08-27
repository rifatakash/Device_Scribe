# Device_Scribe
DeviceScribe is a simple web application for managing company devices, employees, and device usage logs. It provides an API for listing companies, employees, devices, and device logs, along with user authentication and authorization features.

## Features

Company Management: Easily add, edit, and remove company details. Keep track of all companies associated with the system.

Employee Tracking: Manage employee information effortlessly. Link employees to their respective companies and access their details whenever needed.

Device Inventory: Maintain a comprehensive inventory of devices used by companies. Each device includes a name and its corresponding company.

Device Log Recording: Track device usage through comprehensive logs. Monitor when devices are checked out, returned, and their condition.

API Integration: Use Django RESTful APIs to seamlessly integrate DeviceScribe data into other applications or services.

User Authentication: Secure the system with user authentication. Users can register, log in, and access authorized features.

Role-based Authorization: Assign different roles to users, such as administrators and regular users. Control access to specific features based on roles.

Admin Panel: Leverage the Django admin panel for easy data management. Administrators can manage records efficiently.

## Getting Started

1. Clone the repository.
2. Configure settings in `settings.py`.


## API Documentation
DeviceScribe offers a range of Django RESTful APIs to interact with the system programmatically. Below are the API endpoints along with their descriptions:

Companies
Endpoint: /api/companies/
Method: GET
Description: Retrieve a list of all companies.

Employees
Endpoint: /api/employees/
Method: GET
Description: Retrieve a list of all employees.

Devices
Endpoint: /api/devices/
Method: GET
Description: Retrieve a list of all devices.

Device Logs
Endpoint: /api/device-logs/
Method: GET
Description: Retrieve a list of all device logs.
