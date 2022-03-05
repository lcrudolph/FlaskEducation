#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

#from flask import Flask
#app = Flask(__name__)
from Project import app

@app.route("/")
def hello():
    """Testing a method that is the default page of the site"""
    return app.send_static_file("index.html")
