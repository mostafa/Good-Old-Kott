# -*- coding: utf-8 -*-
"""RESTful API for exposing Kott functionality"""

from flask import Flask, jsonify
import gevent.pywsgi
from kott import Kott
from .kconf import __kott_version__
from .kexception import kException


def kREST(host='0.0.0.0', port=9500):
    flask_app = Flask(__name__)

    @flask_app.route("/")
    def index():
        return jsonify({"result":
                        "Welcome to Kott (v." + __kott_version__ + ")"})

    @flask_app.route("/<key>", methods=["GET"])
    def get(key):
        return_data = ""
        try:
            return_data = Kott.get(key)
        except kException as e:
            return_data = str(e)
        return jsonify({"result": return_data})

    @flask_app.route("/<data>", methods=["POST"])
    def set(data):
        key = Kott.set(data)
        return jsonify({"result": key})

    def run_server(host='0.0.0.0', port=9500):
        print("Running server on " + host + ":" + str(port))
        gevent_server = gevent.pywsgi.WSGIServer(
            (host, port), flask_app)
        gevent_server.serve_forever()

    return run_server(host=host, port=port)
