This is a simple api made with python, django and postgresql.

Using this project is quite simple, you will need installed on your machine:
  - python-3.6
  - postgresql-10
  - postgresql-dev-10
  - python3-dev

The steps to use the project are the following:

1) Clone the repository.
2) Access the vuttr folder.(This is the main project folder)
3) Create a virtualenv.(e.g. python3 -m venv .venv)
4) Install the requirements with pip.(e.g. pip install -r requirements.txt)
5) Create a .env file on the main vuttr folder, and set the following variables:
    SECRET_KEY=<your-secret-key>(You can generate one using: python manage.py generate_secret_key)
    DEBUG=<True or False>(Only use False if your planning on running this on production mode, if that's the case remember to set ALLOWED_HOSTS on settings.py)
    DB_NAME=<your-db-name>
    DB_USER=<your-db-user>(With the correct permissions to manage your database)
    DB_PASSWORD=<your-db-user-password>
    DB_HOST=<your-db-host-ip-address>
    DB_PORT=<your-db-host-port>
6) Run python manage.py migrate to create the database.
7) Run python manage.py test(If everything passes you're good to go! If something fails, check the steps above and see if you perhabs missed something. In case you have any doubts about this steps or if you encounter many errors in the installation process feel free to contact me, my email is miguelvellasco@gmail.com)