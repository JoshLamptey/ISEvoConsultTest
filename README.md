
Step-by-Step Documentation to Set Up the Repository

1. Clone the Repository Open your terminal and clone the repository using:

git clone https://github.com/JoshLamptey/ISEvoConsultTest.git
cd ISEvoConsultTest


2. Set Up a Virtual Environment It’s best to use a virtual environment to manage dependencies.

python -m venv env
source env/bin/activate  # On Windows, use env\Scripts\activate


3. Install Dependencies Use the requirements.txt file to install all necessary Python packages:

pip install -r requirements.txt


4. Set Up the Database Run the following commands to set up the database:

python manage.py makemigrations
python manage.py migrate


5. Create a Superuser (Admin Account) To access the Django admin panel, create a superuser:

python manage.py createsuperuser


6. Run the Development Server Start the server using:

python manage.py runserver

Access the application at http://127.0.0.1:8000.




Notes

Ensure settings.py is configured properly (e.g., database settings, middleware for multi-tenancy, etc.).

If your project uses .env files for sensitive information, include an example .env file (e.g., example.env) with placeholders.

