# Django To-do App with User Authentication
## A simple Django-based to-do app with user authentication.

List of contents:
- [Screenshots:](#screenshots)
- [Setup:](#setup)



### Screenshots:

![homepage](static/screenshots/Screenshot%202022-06-09%20at%2007-41-50%20TodoApp%20Tasks.png)
![Login](static/screenshots/Screenshot%202022-06-09%20at%2007-02-22%20TodoApp%20Login.png)
![Signup](static/screenshots/Screenshot%202022-06-09%20at%2007-02-46%20TodoApp%20Create%20Your%20Account.png)

### Setup:

In your git-enabled terminal, type the following command:
```bash
$ https://github.com/Inayatullahsh/Django_auth_todo_app.git
```

Go to the cloned repo directory and run the following command to install the requirements:
```bash
$ pip install -r requirements.txt
```
now run the following command to create the necessary database migrations.
```bash
$ python manage.py makemigrations
```
To apply migrations, run the following command.
```bash
$ python manage.py migrate
```

Finally, run the following command to create a superuser, so you can access the admin interface and provide your `username`, `email`, and `password`.
```bash
$ python manage.py createsuperuser
```
To make the app live, run the following command:
```bash
$ python manage.py runserver
```
and now navigate to http://127.0.0.1:8000 in your browser.

__Happy coding!__

<a href="https://twitter.com/IUShinwari">
<img src="static/screenshots/bmc-button.svg" width="200">
</a>
