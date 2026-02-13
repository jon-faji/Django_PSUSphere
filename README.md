# PSUSphere

## Short Description
PSUSphere is a Django-based web application designed to manage student organizations, programs, and colleges. Administrators can efficiently create, view, and manage colleges, programs, organizations, students, and memberships using a user-friendly Django admin interface.

## Features
- **Manage Colleges**: Add, edit, and search colleges.  
- **Manage Programs**: Associate programs with colleges and search/filter programs.  
- **Manage Organizations**: Create student organizations linked to colleges.  
- **Manage Students**: Add student information, assign programs, and track memberships.  
- **Organization Memberships**: Record student memberships in organizations with join dates.  
- **Enhanced Admin Interface**: Searchable lists, filters, and custom display columns for all models.  
- **Data Seeding**: Use Faker to generate initial sample data for testing.  
- **Version Control Ready**: `.gitignore` prevents sensitive files and virtual environment from being pushed.

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd PSUSphere
```

### 2. Create and activate a virtual environment
```bash
python -m venv psusenv
psusenv\Scripts\activate  # Windows
source psusenv/bin/activate  # Linux/MacOS
```

### 3. Install required packages
```bash
pip install -r requirements.txt
```

### 4. Apply database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser to access the admin panel
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

### 7. Access the admin panel
Open [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) in your browser and log in with your superuser credentials.

## Authors
- Jon Faji
- jasperOlpos27
