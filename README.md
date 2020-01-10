Named Entity Recognition API
===

This API could be asked as follows :

`POST /api/v1/entities`

```
{
  "language":"fr",
  "text": "Mon nom est Jo Hisahi"
}
```

The 200 response would answer :

```
{
  "entities": [
    {
      "entity": {
        "start": 12,
        "end": 21,
        "type": {
          "name": "flair:person"
        }
      },
      "probability": 0.9251298308372498
  ]
}
```

Using of Python Flask library on `v1`.

Contribute
===

First, use `virtualenv venv` then `source venv/bin/activate` and `pip install -r requirements.txt` for development.
Start the WSGI with `FLASK_ENV=development python handler.py` in development mode.

Docker
===

Dockerfile provided for deployment.
Production mode : https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html
Production mode with Docker : https://aws.amazon.com/fr/blogs/devops/dockerizing-a-python-web-app/