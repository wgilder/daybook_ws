from flask import jsonify, request, _request_ctx_stack, render_template
from app import app
from streifen.ws.daybook.version import Version
from streifen.ws.daybook.item import Item
from streifen.ws.daybook.user import User

@app.route('/v1/version')
def version():
    v = Version()
    attrs = v.attributes()
    template = v.template_name()
    return render_template(template, **attrs)

@app.route('/v1/item', methods=[ 'PUT' ])
@app.route('/v1/item/<int:id>', methods=[ 'PATCH', 'GET' ])
def item(id = -1):
    if request.method == 'PUT':
        title = request.form['title']

    return

@app.route('/v1/items/<int:page>', methods=[ 'GET' ])
@app.route('/v1/items', methods=[ 'GET' ])
def items(page = 0):
    return []

@app.route('/test')
def test():
    user = User()
    user.set_email("user@example.com")
    user.set_name("John Q. Public")
    item = Item(user)
    item.serialize()
    return "Done."