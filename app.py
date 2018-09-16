from flask import Flask
from ddtrace import tracer
from ddtrace.contrib.flask import TraceMiddleware

app = Flask(__name__)
tracer.configure(hostname='172.17.0.1', port=8126)
traced_app = TraceMiddleware(app, tracer, service="daybook_ws", distributed_tracing=False)

from streifen.ws.daybook import routes
