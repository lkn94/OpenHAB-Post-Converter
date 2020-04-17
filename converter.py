from flask import Flask, request
from flask_restful import Api
import requests

app = Flask(__name__)
api = Api(app)

openhab = "192.168.XXX.XX:8080"

@app.route('/')
def main():
    return "Change GET-Requests to POST-Requests for OpenHAB"

@app.route('/item')
def item():
    name = request.args.get("name")
    state = request.args.get("state")
    if (name != "" and state != ""):
        response = requests.post("http://{}/rest/items/{}".format(openhab, name), data=state)
        return "{}".format(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008, debug=False)
