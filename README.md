# roomly
Web app for finding and booking free classes and labs.# Roomly

Web app for finding and booking free classes and labs.

## How to run

1. Install Python and MySQL Server.
2. Create a virtual environment and install the packages:
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
3. Create a .env file with DB_HOST, DB_USER, DB_PASSWORD, DB_NAME and SECRET_KEY.
4. Create the database: python database\setup_db.py
5. Start the site: python run.py
6. Open http://127.0.0.1:5000