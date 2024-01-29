# Bindu Blood Bank
A blood bank website using django framework.

## Features
- Unauthenticated user can open an account, view homepage.
- Authenticated user can login, logout, view profile, update profile information, change password, request for blood, donate blood.
- Superuser or admin or staff can do all what an Authenticated user can. Also can add services.


## Deployment

The first thing to do is to clone the repository:

```bash
  git clone https://github.com/tanzid64/blood-bank.git
  cd blood-bank
```
Create a virtual environment to install dependencies in and activate it:

```bash
  python -m venv .venv
  .venv\Scripts\activate
```
Then install the dependencies:

```bash
  pip install -r requirements.txt
```
Create a file name .env in project folder. Use Posgresql as database, and gmail account as email account. Setup your .env as per the requirements.

Apply migrations:

```bash
  python manage.py migrate
```
Create an admin account:

```bash
  python manage.py createsuperuser
```
Start the django application::

```bash
  python manage.py runserver
```

That's it! You should now be able to see the demo application.
Browse:
- HomePage:  localhost:8000/
- Admin Panel:  localhost:8000/admin


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`
`EMAIL_HOST_USER`
`EMAIL_HOST_PASSWORD`
`DATABASE_LINK`


