<h1>Very Useful Tools To Remember</h1>

<h4>This is a simple api made with python, django and postgresql, to manage tools you want to remember or study.</h4>

Using this project is quite simple, you will need installed on your machine:
  - python-3.6
  - postgresql-10
  - postgresql-dev-10
  - python3-dev

The steps to use the project are the following:

1) Clone the repository.
2) Access the vuttr_project folder.(This is the main project folder)
3) Create a virtualenv.(e.g. python3 -m venv .venv)
4) Activate your virtual environment with: source .venv/bin/activate
5) Install the requirements with pip.(e.g. pip install -r requirements.txt)
6) Create a .env file on the vuttr_project folder, and set the following variables:
    - SECRET_KEY=your-secret-key (First set it to any value(e.g. abc) and after that create a real one using python manage.py generate_secret_key and replace the old value with the created one.)
    - DEBUG=True or False (Only use False if your planning on running this on production mode, if that's the case remember to set ALLOWED_HOSTS on settings.py)
    - DB_NAME=your-db-name
    - DB_USER=your-db-user (With the correct permissions to manage your database)
    - DB_PASSWORD=your-db-user-password
    - DB_HOST=your-db-host-ip-address-or-FQDN
    - DB_PORT=your-db-host-port
7) Run python manage.py migrate to create the database.
8) Run python manage.py loaddata initial_tools.json to populate the database with some tools.
9) Run python manage.py test(If everything passes you're good to go! If something fails, check the steps above and see if you perhabs missed something. In case you have any doubts about these steps or if you encounter many errors in the installation process feel free to contact me, my email is miguelvellasco@gmail.com)
10) Run python manage.py runserver localhost:3000 to fire-up the development server, so you can see the api in action.
