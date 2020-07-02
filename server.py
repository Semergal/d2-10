import sentry_sdk
import os
from bottle import Bottle, request, route, run
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://351c23bf47094413bb7164bf49a60488@o414592.ingest.sentry.io/5305525",
    integrations=[BottleIntegration()]
)

app = Bottle()
@app.route("/success")
def index():
    html = """<p>Success</p>"""
    return html

@app.route("/")
def index():
    html = """<p>Main page</p>"""
    return html


@app.route('/fail')
def index():
    raise RuntimeError("500 Error!")


if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8080, debug=True)