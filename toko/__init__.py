from flask import Flask
from toko.config import Config
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)


app.config.from_object(Config)

db = SQLAlchemy(app)

#created models
from toko.models import Pegawai

#created url
from toko import routes