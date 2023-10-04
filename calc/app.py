# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }


@app.route("/math/<op>")
def do_math_math(op):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[op](a, b)

    return str(result)


@app.route("/<op>")
def do_math(op):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[op](a, b)

    return str(result)

