# Setup Guide for SmartHomeCloset Web Application

This guide provides step-by-step instructions for setting up the SmartHomeCloset web application, including the installation of Django, PostgreSQL, and necessary Python libraries. Follow these instructions carefully to get the application running on your local machine.

## Prerequisites

Before you begin, ensure you have the following installed on your Mac:

- **Homebrew**: A package manager for macOS. If you don't have it installed, you can install it by running:
  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```

- **Create Necessary Files and Folders**:
  ```bash
  cd ./SmartHomeCloset/
  mkdir -p media/Outfits
  ```

## Step 1: Install PostgreSQL

1. **Download PostgreSQL**: 
   - Go to [Postgres.app](https://postgresapp.com/) and download the latest version (PostgreSQL 17 in your case).
   - Open the downloaded `.dmg` file and drag the PostgreSQL icon to your Applications folder.

2. **Start PostgreSQL**:
   - Open Postgres.app from your Applications folder. This will start the PostgreSQL server.

3. **Create a Database**:
   - Open the terminal and run the following command to access the PostgreSQL command line:
     ```bash
     psql postgres
     ```
   - Create a new database for your application:
     ```sql
     CREATE DATABASE webappdb;
     ```
   - Exit the PostgreSQL command line:
     ```sql
     \q
     ```

## Step 2: Set Up Python and Virtual Environment

1. **Install Python**:
   - If you don't have Python installed, you can install it using Homebrew:
     ```bash
     brew install python
     ```

2. **Create a Virtual Environment**:
   - Navigate to the directory where you want to store your project:
     ```bash
     cd path/to/your/project
     ```
   - Create a virtual environment:
     ```bash
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     ```bash
     source venv/bin/activate
     ```

## Step 3: Install Required Python Libraries

1. **Upgrade pip**:
   - Ensure you have the latest version of pip:
     ```bash
     pip install --upgrade pip
     ```

2. **Install Django and Other Libraries**:
   - Install Django, Pillow, and other required libraries:
     ```bash
     pip install django pillow psycopg2-binary django-environ
     ```

## Step 4: Clone the SmartHomeCloset Repository

1. **Clone the Repository**:
   - If you haven't already, clone the SmartHomeCloset repository from your version control system (e.g., GitHub):
     ```bash
     git clone https://github.com/yourusername/SmartHomeCloset.git
     cd SmartHomeCloset
     ```

## Step 5: Configure the .env File

1. **Create the .env File**:
   - In the `SmartHomeCloset/SmartHomeCloset/` directory of your project (where `manage.py` is located), create a new file named `.env`:
     ```bash
     touch .env
     ```

2. **Add Configuration Variables**:
   - Open the `.env` file in a text editor and add the following lines, replacing the values as necessary:
     ```plaintext
        SECRET_KEY=django-insecure-YOUR-SECRET-KEY
        DB_NAME=Name of Database
        DB_USER=Database USER(should be Postgres by default)
        DB_PASSWORD=Database Password for user
        DB_HOST=Host
        DB_PORT=PortNumber
     ```

## Step 6: Run Migrations

1. **Apply Migrations**:
   - Ensure you are still in the virtual environment and in the project directory. Run the following command to apply migrations and set up the PostgreSQL schema:
     ```bash
     python manage.py migrate
     ```

2. **Create a Superuser** (optional):
   - If you want to access the Django admin interface, create a superuser account:
     ```bash
     python manage.py createsuperuser
     ```
   - Go `http://127.0.0.1:8000/admin/` to access the Django Admin portal

## Step 7: Run the Development Server

1. **Start the Development Server**:
   - Run the following command to start the Django development server:
     ```bash
     python manage.py runserver
     ```

2. **Access the Application**:
   - Open your web browser and navigate to `http://127.0.0.1:8000/` to access the SmartHomeCloset application.

## Conclusion

You have successfully set up the SmartHomeCloset web application on your local machine. You can now explore the features of the application, register closets, manage clothing items, and more. If you encounter any issues, refer to the documentation for Django and PostgreSQL, or seek help from the community. Happy coding!
