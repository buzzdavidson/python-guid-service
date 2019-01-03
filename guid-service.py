from flask import Flask
import sys
import optparse
import time
import uuid

app = Flask(__name__)

start = int(round(time.time()))

def get_uuid_string():
    return str(uuid.uuid4())

@app.route("/api/v1/guid/text")
def get_plaintext_guid():
    return get_uuid_string();

@app.route("/")
def get_default_page():
    return "<h1>Catalog</h1><p>This service builds UUIDs!</p><p>You probably want <a href='/api/v1/guid/text'>/api/v1/guid/text</a></p>"

if __name__ == '__main__':
    parser = optparse.OptionParser(usage="python simpleapp.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port == None:
        print "Missing required argument: -p/--port"
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=False)