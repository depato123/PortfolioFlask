from flask import Flask, render_template, request, redirect, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import hashlib
import os
import json

app = Flask(__name__)
#app.config.from_object('app.config')
db = SQLAlchemy(app)

@app.route("/index")
def inicio():
    return render_template('index.html')