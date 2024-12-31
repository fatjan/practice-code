from flask import Flask, request
from werkzeug.exceptions import MethodNotAllowed, Forbidden

app = Flask(__name__)

def check_method(request, method):
    if request.method != method:
        raise MethodNotAllowed()

banner = ""

@app.route("/echo", methods=["GET"])
def echo():
    check_method(request, "GET")

    args = request.args
    for key in request.args:
        print(key)

    message = args.get("message")
    if (message is None):
        return "NOT ACCEPTABLE", 406

    resp = Flask.Response(message)
    resp.headers["banner"] = banner
    return resp

@app.route("/set_banner", methods=["POST"])
def admin():
    check_method(request, "POST")

    headers = request.headers
    if "auth" not in headers:
        raise Forbidden()

    auth = headers["admin-auth"]
    if auth != '1234':
        raise Forbidden()
    
    banner = request.data['banner']

    return


if __name__ == '__main__':
    # do not change the ip nor the port that is used for the app
    app.run(host='127.0.0.1', port=8080)
