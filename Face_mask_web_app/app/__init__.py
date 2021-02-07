# -*- coding: utf-8 -*-
"""
INITIALIZING THE APP
"""

from flask import Flask

app = Flask(__name__)
app.secret_key = "abcd"

from app import routes
from app import register
from app import userpage
from app import history
from app import api_upload
from app import api_register
from app import pass_rec
from app import delete
