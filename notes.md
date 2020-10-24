Users   |   Passwords
susan       cat
sam         dog
jack        boo
eric        yoo
mayra       hey
bob         who

pip freeze > requirements.txt

pip install -r requirements.txt

flask shell

In Chapter 3 I showed you a first Flask extension. In this chapter I'm going to use two more. 
The first is Flask-SQLAlchemy, an extension that provides a Flask-friendly wrapper to the popular SQLAlchemy package, which is an Object Relational Mapper or ORM. 
ORMs allow applications to manage a database using high-level entities such as classes, objects and methods instead of tables and SQL. 
The job of the ORM is to translate the high-level operations into database commands.
The nice thing about SQLAlchemy is that it is an ORM not for one, but for many relational databases. 
SQLAlchemy supports a long list of database engines, including the popular MySQL, PostgreSQL and SQLite. 
This is extremely powerful, because you can do your development using a simple SQLite database that does not require a server, 
and then when the time comes to deploy the application on a production server you can choose a more robust MySQL or PostgreSQL server, 
without having to change your application.


The second extension that I'm going to present in this chapter is Flask-Migrate, which is actually one created by yours truly. 
This extension is a Flask wrapper for Alembic, a database migration framework for SQLAlchemy. 
Working with database migrations adds a bit of work to get a database started, 
but that is a small price to pay for a robust way to make changes to your database in the future.

SQLite database
    flask db migrate - Since I have updates to the application models, a new database migration needs to be generated:
    flask db upgrade - And the migration needs to be applied to the database:
    flask db downgrade

[DB Browser for SQLite] to visually see our database

Hash passwords
One of the packages that implement password hashing is Werkzeug, which you may have seen referenced 
in the output of pip when you install Flask, since it is one of its core dependencies

    hashes password - hash = generate_password_hash('foobar')
    verification process - check_password_hash(hash, 'foobar') -> true

In this chapter I'm going to introduce you to a very popular Flask extension called Flask-Login. This extension manages the user logged-in state, so that for example users can log in to the application and then navigate to different pages while the application "remembers" that the user is logged in. It also provides the "remember me" functionality that allows users to remain logged in even after closing the browser window.

The Flask-Login extension works with the application's user model, and expects certain properties and methods to be implemented in it. This approach is nice, because as long as these required items are added to the model, Flask-Login does not have any other requirements, so for example, it can work with user models that are based on any database system.

The four required items are listed below:

    is_authenticated: a property that is True if the user has valid credentials or False otherwise.
    is_active: a property that is True if the user's account is active or False otherwise.
    is_anonymous: a property that is False for regular users, and True for a special, anonymous user.
    get_id(): a method that returns a unique identifier for the user as a string (unicode, if using Python 2).


Flask-Login keeps track of the logged in user by storing its unique identifier in Flask's user session, a storage space assigned to each user who connects to the application. Each time the logged-in user navigates to a new page, Flask-Login retrieves the ID of the user from the session, and then loads that user into memory.

Because Flask-Login knows nothing about databases, it needs the application's help in loading a user. For that reason, the extension expects that the application will configure a user loader function, that can be called to load a user given the ID. This function can be added in the app/models.py module

The way Flask-Login protects a view function against anonymous users is with a decorator called @login_required. When you add this decorator to a view function below the @app.route decorators from Flask, the function becomes protected and will not allow access to users that are not authenticated. Here is how the decorator can be applied to the index view function of the application: