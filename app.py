from flask import Flask
app = Flask(__name__)
from streifen.ws.daybook import routes
