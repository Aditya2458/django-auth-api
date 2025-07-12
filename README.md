Django Authentication API
A secure and scalable RESTful authentication API built using Django and Django REST Framework (DRF). This API handles user registration, login, logout, password management, and token-based authentication using JWT.

🚀 Features
User Registration (Sign Up)

User Login (with JWT token generation)

User Logout

Password Change & Reset

JWT-based Authentication (access and refresh tokens)

Token Blacklisting on Logout

User Profile View

Email validation support (optional)

DRF Permissions & Authentication Classes

🛠 Tech Stack
Backend: Django, Django REST Framework (DRF)

Authentication: JWT (via djangorestframework-simplejwt)

Database: SQLite (default), supports PostgreSQL/MySQL

Environment: Python 3.x, Django 4+

📁 Project Structure
bash
Copy
Edit
auth_api_project/
├── users/                  # App handling user auth
│   ├── views.py            # API views for login, register, etc.
│   ├── serializers.py      # DRF serializers
│   ├── urls.py             # API endpoints
├── auth_api_project/
│   ├── settings.py         # JWT, DRF setup
├── requirements.txt
├── manage.py
⚙️ Installation
bash
Copy
Edit
# Clone the repository
git clone https://github.com/yourusername/django-auth-api.git
cd django-auth-api

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
🔐 API Endpoints
Method	Endpoint	Description
POST	/api/register/	Register a new user
POST	/api/token/	Get JWT tokens
POST	/api/token/refresh/	Refresh access token
POST	/api/token/blacklist/	Logout & blacklist token
GET	/api/profile/	Get user profile

📦 Requirements
shell
Copy
Edit
Django>=4.0
djangorestframework
djangorestframework-simplejwt
📌 Notes
Make sure to add .env for secret keys and sensitive settings.

You can switch to PostgreSQL/MySQL in settings.py for production.

Set up email backend for password reset via email.

📜 License
MIT License
