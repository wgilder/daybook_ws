from flask import render_template
from app import app
from streifen.ws.daybook.version import Version
import pystache

@app.route('/v1/version')
def version():
    v = Version()
    renderer = pystache.Renderer()
    return renderer.render(v)
