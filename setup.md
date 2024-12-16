# Setup Guide for SmartHomeCloset Local Network Configuration

This section provides instructions for installing and configuring PostgreSQL on a Raspberry Pi to accept local connections.

### Prerequisites

- A Raspberry Pi running Raspberry Pi OS (formerly Raspbian).
- Access to the terminal (either directly or via SSH).
- An active internet connection for the Raspberry Pi.

### Step 1: Update Your System

Before installing PostgreSQL, ensure that your Raspberry Pi is up to date. Open the terminal and run the following commands:

```bash
sudo apt update
sudo apt upgrade -y
```

### Step 2: Install PostgreSQL

1. **Install PostgreSQL**: Use the following command to install PostgreSQL and the necessary packages:

   ```bash
   sudo apt install postgresql postgresql-contrib -y
   ```

2. **Check PostgreSQL Status**: After installation, check if PostgreSQL is running:

   ```bash
   sudo systemctl status postgresql
   ```

   You should see an output indicating that the service is active (running). If it is not running, you can start it with:

   ```bash
   sudo systemctl start postgresql
   ```

### Step 3: Configure PostgreSQL to Accept Local Connections

1. **Edit the PostgreSQL Configuration File**: Open the `postgresql.conf` file to allow connections from your local network. Use the following command:

   ```bash
   sudo nano /etc/postgresql/*/main/postgresql.conf
   ```

2. **Find the `listen_addresses` Line**: Look for the line that starts with `listen_addresses`. By default, it may be set to `localhost`. Change it to:

   ```plaintext
   listen_addresses = '*'
   ```

   This setting allows PostgreSQL to accept connections from any IP address.

3. **Save and Exit**: Press `CTRL + X`, then `Y`, and hit `Enter` to save the changes and exit the editor.

### Step 4: Configure Client Authentication

1. **Edit the `pg_hba.conf` File**: Open the `pg_hba.conf` file to configure client authentication:

   ```bash
   sudo nano /etc/postgresql/*/main/pg_hba.conf
   ```

2. **Add a Local Network Entry**: At the end of the file, add the following line to allow connections from your local network (replace `192.168.1.0/24` with your actual local network range):

   ```plaintext
   host    all             all             192.168.1.0/24          md5
   host    all             all             127.0.0.1/32          md5
   ```

   This line allows all users to connect to all databases from any IP address in the `192.168.1.0/24` subnet using password authentication.
    Note: You can find your local network range by finding out your device's local ip address e.g. `192.168.1.111`, and extracting the first 24 bits from it e.g. `192.168.1.0`.
 
3. **Save and Exit**: Press `CTRL + X`, then `Y`, and hit `Enter` to save the changes and exit the editor.

### Step 5: Restart PostgreSQL

After making the configuration changes, restart the PostgreSQL service to apply them:

```bash
sudo systemctl restart postgresql
```

### Step 6: Create a PostgreSQL User and Database

1. **Access the PostgreSQL Command Line**: Switch to the PostgreSQL user:

   ```bash
   sudo -i -u postgres
   ```

2. **Open the PostgreSQL Shell**:

   ```bash
   psql
   ```

3. **Create a New User**: Replace `your_username` and `your_password` with your desired username and password:

   ```sql
   CREATE USER your_username WITH PASSWORD 'your_password';
   ```

4. **Create a New Database**: Replace `your_database` with your desired database name:

   ```sql
   CREATE DATABASE your_database WITH OWNER your_username;
   ```

5. **Grant Privileges**: Allow the new user to access the database:

   ```sql
   GRANT ALL PRIVILEGES ON DATABASE your_database TO your_username;
   ```

6. **Exit the PostgreSQL Shell**:

   ```sql
   \q
   ```

7. **Exit the PostgreSQL User**:

   ```bash
   exit
   ```

#### Step 6b(optional): Connect using PgAdmin4
1. Right-click on Servers and navigate to `Register` then, `Servers`.
2. Enter the name of connection in the `General` tab.
3. Navigate to the `Connection` tab.
    ```plain text
    Host name/address - Your Pi's Local Ip Address
    Port - 5432
    Maintenance database - postgres
    Username - postgres
    Password - Your postgres user password
    ```
4. Hit Save.

### Step 7: Test the Connection

1. **Test the Connection from Another Device**: From another device on the same local network, you can test the connection using the `psql` command:

   ```bash
   psql -h <Raspberry_Pi_IP_Address> -U your_username -d your_database
   ```

   Replace `<Raspberry_Pi_IP_Address>` with the actual IP address of your Raspberry Pi.

2. **Enter the Password**: When prompted, enter the password you set for the PostgreSQL user.

### IMPORTANT NOTE:
Make sure to update the `SmartHomeCloset/SmartHomeCloset/.env` fields with respect to the database on your pi you just created.


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
        SECRET_KEY=YOUR-SECRET-KEY
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
     python manage.py makemigrations
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

