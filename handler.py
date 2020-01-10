from flask import Flask, request, jsonify
from ner import get_flair, evaluate
import json
from errors import *

app = Flask(__name__)


@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


@app.route("/api/v1/entities", methods=["POST"])
def get():
    if request.content_type == "application/json":
        body = json.loads(request.data) if request.data else {}

        language = body["language"] if "language" in body.keys() else None
        if not language:
            raise LanguageMandatory()
        flair = get_flair(language)
        if not flair:
            raise LanguageInvalid()

        content = body["text"] if "text" in body.keys() else None
        if not content:
            raise TextMandatory()

        return evaluate(flair, content)

    else:
        raise InvalidUsage()


if __name__ == "__main__":
    app.run(port="5000")
