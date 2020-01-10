from flask import jsonify
from werkzeug.exceptions import HTTPException

class LanguageInvalid(HTTPException):
    code = 400
    description = "language invalid. fr or en only"

class LanguageMandatory(HTTPException):
    code = 400
    description = "language key must be present in body"

class TextMandatory(HTTPException):
    code = 400
    description = "text key must be present in body"

class InvalidUsage(HTTPException):
    code = 400
    description = "JSON body mandatory with language and text keys"