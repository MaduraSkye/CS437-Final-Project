# Smart Home Closet

SmartHomeCloset is a web application designed to help users manage their closets, clothing items, and outfits efficiently. Built using Django and PostgreSQL, this application allows users to register closets, add clothing items, and create outfits, all while providing a user-friendly interface.

## Features

- **User Authentication**: Secure login and registration for users.
- **Closet Management**: Users can create, view, and remove closets.
- **Clothing Item Management**: Add, view, and remove clothing items associated with closets.
- **Outfit Creation**: Users can create outfits by selecting clothing items from their registered closets.
- **Responsive Design**: The application is designed to be user-friendly on both desktop and mobile devices.

## Technologies Used

- **Django**: A high-level Python web framework for rapid development.
- **PostgreSQL**: A powerful, open-source relational database system.
- **HTML/CSS**: For structuring and styling the web application.
- **JavaScript**: For interactive elements and AJAX functionality.
- **Bootstrap**: For responsive design and layout.

## Installation

### Prerequisites

- Python 3.x
- PostgreSQL
- pip (Python package installer)
- Homebrew (for macOS users)

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/SmartHomeCloset.git
   cd SmartHomeCloset
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Required Libraries**:
   ```bash
   pip install django pillow psycopg2-binary django-environ
   ```

4. **Configure PostgreSQL**:
   - Install PostgreSQL and create a database for the application.
   - Update the `.env` file with your database credentials.

5. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**:
   - Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- Register a new closet and add clothing items.
- Create outfits by selecting items from your registered closets.
- Manage your closets and outfits through the user interface.


## Acknowledgments

- Thanks to the Django community for their excellent documentation and support.
- Special thanks to the contributors who help improve this project.