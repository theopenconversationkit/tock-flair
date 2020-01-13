Named Entity Recognition API
===

This API has this endpoint :

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

Using Flair library on `v1` for NER.

## Contribute

First, use `virtualenv venv` then `source venv/bin/activate` and `pip install -r requirements/dev.txt` for development.
Download the models with the script in `build/download_models.sh`.
Start the WSGI with `FLASK_ENV=development python application.py` in development mode.

## Docker

Dockerfile provided for deployment.
Build : `docker build -t name .`
Run local : `docker run -p 8080:5000 name`
On Amazon : https://aws.amazon.com/fr/blogs/devops/dockerizing-a-python-web-app/