import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext
import json

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    seed_db()
    click.echo('Initialized the database.')

def seed_db():
    f = open('results.json', 'r')
    data = json.load(f)
    results = []

    for i in range(len(data['results'])):
        result = data['results'][i]
        gender = result['gender']
        firstName = result['name']['first']
        lastName = result['name']['last']
        city = result['location']['city']
        postCode = result['location']['postcode']
        email = result['email']
        username = result['login']['username']
        birthdate = result['dob']['date']
        phone = result['phone']
        imageName = f"{i + 1}.jpg"
        results.append((gender, firstName, lastName, city, postCode, email, username, birthdate, phone, imageName))
    connection = get_db()
    connection.executemany('INSERT INTO user(gender, firstName, lastName, city, postCode, email, username, birthdate, phone, imageName) VALUES(?,?,?,?,?,?,?,?,?,?);', results)
    connection.commit()


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
