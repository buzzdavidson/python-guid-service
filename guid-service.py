from flask import Flask, request
import sys
import optparse
import time
import uuid
import json

app = Flask(__name__)

start = int(round(time.time()))

def get_uuid_string():
    return uuid.uuid4().hex

@app.route("/api/v1/guid/text")
def get_plaintext_guid_text():
    return get_uuid_string();

@app.route("/api/v1/guid")
def get_plaintext_guid_json():
    c = request.args.get("count")
    if c is None:
        c = "1"
    count=int(c)
    values = []
    for x in xrange(count):
        values.append(get_uuid_string())
        
    return json.dumps(values);

@app.route("/")
def get_default_page():
    return "<h1>GUID Service</h1><p>UUID Generation Service</p><ul><li><a href='/api/v1/guid/text'>/api/v1/guid/text (plaintext)</a></li><li><a href='/api/v1/guid'>/api/v1/guid (JSON) - NOTE: accepts count parameter</a></li></ul>"

if __name__ == '__main__':
    parser = optparse.OptionParser(usage="python simpleapp.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port == None:
        print "Missing required argument: -p/--port"
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=False)
