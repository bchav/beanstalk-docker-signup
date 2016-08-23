# Copyright 2015. Amazon Web Services, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# sample commit
import os
import sys
import json

import flask
from flask import request, Response

from redis import Redis

# Create the Flask app
app = flask.Flask(__name__)
redis = Redis(host='your_elasticache_node_endpoint', port=6379)

@app.route('/')
def welcome():
    return flask.render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    signup_data = dict()
    for item in request.form:
        signup_data[item] = request.form[item]

    if redis.exists(signup_data['email']):
        return Response("", status=409, mimetype='app/json')
    else:
        redis.set(signup_data['email'], 'true')

    return Response(json.dumps(signup_data), status=201, mimetype='app/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
