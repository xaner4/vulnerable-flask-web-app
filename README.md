# vulnerable flask web app

A vulnerable web app for testing purposes

## Install and start flask application

Install pipenv on your system

```bash
pip install --user pipenv
```

Install the python packages

```bash
pipenv install
```

Rename .env.example file to .env 
```bash
mv .env.example .env
```

Change values if needed in the .env file


Init the database

```bash
flask init-db
```

start the flask app
```bash
flask run
```

PS. test data is not automaticly importet, but it can be done with the use of something like [sqlite browser](https://sqlitebrowser.org/)
