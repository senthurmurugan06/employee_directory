# Mini Employee Directory - Django Web App

A dynamic Employee Directory system built with Django, featuring AJAX interactions, Bootstrap UI, and RESTful API endpoints.

## Features

**Dynamic Employee Viewing**: View employees using AJAX and JavaScript fetch API
**Modal Form**: Add new employees via Bootstrap-powered modal without page reload
**Secure API**: Django decorators and session-based authentication
**Django ORM**: All data operations via Django ORM
**Jinja Templates**: UI rendering using Django templating
**Custom Management Command**: `refresh_employees` command to simulate data refresh

##  Tech Stack

- **Backend**: Django 5.2.3, Python
- **Frontend**: HTML/CSS, Bootstrap 5.3.0, JavaScript (Fetch API)
- **Database**: SQLite (Django ORM)
- **Templates**: Django Jinja Templates

## Project Structure

```
mini_employee_directory/
├── employee_directory/          # Main Django project
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Main URL configuration
│   └── ...
├── employees/                  # Employee app
│   ├── models.py              # Employee model
│   ├── views.py               # Views and API endpoints
│   ├── urls.py                # App URL patterns
│   ├── admin.py               # Admin registration
│   └── management/commands/   # Custom management commands
├── templates/employees/        # HTML templates
│   └── employee_directory.html # Main template
├── static/                    # Static files
├── manage.py                  # Django management script
└── README.md                  # This file
```

##  Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone and Setup**:
   ```bash
   cd mini_employee_directory
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install django
   ```

2. **Database Setup**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Populate Sample Data**:
   ```bash
   python manage.py refresh_employees
   ```

4. **Run Development Server**:
   ```bash
   python manage.py runserver
   ```

5. **Access the Application**:
   - Main App: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## API Endpoints

- `GET /api/employees/` - List all employees (AJAX)
- `POST /api/employees/add/` - Add new employee (AJAX)

##  Key Features Implementation

### 1. Dynamic Employee Viewing
- Uses JavaScript Fetch API to load employees asynchronously
- No page reload required for data updates

### 2. Bootstrap Modal Form
- Responsive modal for adding employees
- Form validation and error handling
- Automatic table refresh after successful addition

### 3. Security Features
- CSRF protection (disabled for demo, enable in production)
- Input validation and sanitization
- Session-based authentication ready

### 4. Custom Management Command
- `python manage.py refresh_employees`
- Simulates periodic data refresh
- Useful for testing and development

##  Development Notes

- **CSRF**: Currently disabled for demo purposes. Enable in production
- **Database**: SQLite for development, easily switchable to PostgreSQL/MySQL
- **Static Files**: Configured for development, use `collectstatic` for production

## Future Enhancements

- Employee search and filtering
- Employee editing and deletion
- Department management
- User authentication and authorization
- API rate limiting
- Database optimization

##  Learning Outcomes

This project demonstrates:
- Full-stack Django development
- AJAX integration with Django
- RESTful API design
- Bootstrap UI implementation
- Django ORM usage
- Custom management commands
- Template inheritance and rendering
