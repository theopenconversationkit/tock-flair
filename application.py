from flask import Flask, request, jsonify
from ner import get_flair, evaluate
import json
from errors import *

application = Flask(__name__)


@application.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


@application.route("/api/v1/parse", methods=["POST"])
def parse():
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


@application.route("/api/v1/entities", methods=["GET"])
def entities():
    return jsonify(["flair:person", "flair:location", "flair:organization"]), 200


@application.route("/healthcheck", methods=["GET"])
def healthcheck():
    return '', 200


if __name__ == "__main__":
    application.run(host="0.0.0.0", port="5000")
