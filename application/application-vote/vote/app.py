from flask import Flask, render_template, request, make_response, g
from redis import Redis
from prometheus_client import Counter
# from werkzeug.middleware.dispatcher import DispatcherMiddleware
# from prometheus_client import make_wsgi_app
from prometheus_client import start_http_server
# from prometheus_client.exposition import MetricsHandler
import os
import socket
import random
import json
import logging

REQUESTS = Counter('server_requests_total', 'Total number of requests to this webserver')

option_a = os.getenv('OPTION_A', "Real Madrid")
option_b = os.getenv('OPTION_B', "Barcelona")
hostname = socket.gethostname()

app = Flask(__name__)
# registry = CollectorRegistry()

# counter = Counter('my_flask_app_requests_total', 'Total number of requests', registry=registry)

# app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
#     '/metrics': make_wsgi_app()
# })

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.INFO)

def get_redis():
    if not hasattr(g, 'redis'):
        g.redis = Redis(host="redis", db=0, socket_timeout=5)
    return g.redis

# @app.route('/metrics')
# def metrics():
#     return generate_latest(registry), 200, {'Content-Type': 'text/plain; version=0.0.4'}

@app.route("/", methods=['POST','GET'])
def hello():
    # REQUESTS.inc()
    # counter.inc()
    voter_id = request.cookies.get('voter_id')
    if not voter_id:
        voter_id = hex(random.getrandbits(64))[2:-1]

    vote = None

    if request.method == 'POST':
        redis = get_redis()
        vote = request.form['vote']
        app.logger.info('Received vote for %s', vote)
        data = json.dumps({'voter_id': voter_id, 'vote': vote})
        redis.rpush('votes', data)

    resp = make_response(render_template(
        'index.html',
        option_a=option_a,
        option_b=option_b,
        hostname=hostname,
        vote=vote,
    ))
    resp.set_cookie('voter_id', voter_id)
    return resp

@app.route("/vote", methods=['POST','GET'])
def vote():
    # REQUESTS.inc()
    # counter.inc()
    voter_id = request.cookies.get('voter_id')
    if not voter_id:
        voter_id = hex(random.getrandbits(64))[2:-1]

    vote = None

    if request.method == 'POST':
        redis = get_redis()
        vote = request.form['vote']
        app.logger.info('Received vote for %s', vote)
        data = json.dumps({'voter_id': voter_id, 'vote': vote})
        redis.rpush('votes', data)

    resp = make_response(render_template(
        'index.html',
        option_a=option_a,
        option_b=option_b,
        hostname=hostname,
        vote=vote,
    ))
    resp.set_cookie('voter_id', voter_id)
    return resp

if __name__ == "__main__":
    start_http_server(5050)
    app.run(host='0.0.0.0', port=80, debug=False, threaded=True)
