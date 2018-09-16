from flask import Flask
from ddtrace import tracer
from ddtrace.contrib.flask import TraceMiddleware

app = Flask(__name__)
traced_app = TraceMiddleware(app, tracer, service="daybook_ws", distributed_tracing=False)

from streifen.ws.daybook import routes
