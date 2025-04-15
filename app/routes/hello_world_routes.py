from flask import Blueprint
hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.get("/")
def say_hello_world():
    return "Hello, World!"

@hello_world_bp.get("/hello/JSON")
def say_hello_json():
    return {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }

@hello_world_bp.get("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)

    # The error TypeError: can only concatenate list (not "str") to list should help us refactor our code to get a 200 OK.
    # response_body["hobbies"] + new_hobby

    return response_body
