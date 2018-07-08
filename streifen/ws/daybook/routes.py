from flask import render_template
from app import app
from streifen.ws.daybook.version import Version

def _render(obj):
    attrs = obj.attributes()
    template = obj.template_name()
    return render_template(template, **attrs)

@app.route('/v1/version')
def version():
    v = Version()
    return _render(v)
