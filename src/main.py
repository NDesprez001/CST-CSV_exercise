"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import io
import csv
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "hello": "world"
    }

    return jsonify(response_body), 200

@app.route('/tournaments/upload', methods=['POST'])
def tournament_upload():
    f = request.files['csv']
    f_read = io.StringIO( f.read().decode() )
    file_rows = csv.reader( f_read, delimiter=',' )
    lst = []
    # for x in file_rows:
    #     new_dict = {}
    #     new_dict[x[0]] = {
	# 	    x[0]: 'adljf',
	# 	    x[1]: ';daslkfj',
	# 	    x[2]: 'as;ld',
	# 	    x[3]: 'asds',
	# 	    x[4]: 'skgljs',
	# 	    x[5]: 'disgkj',
	# 	    x[6]: ';dlkjf',
	# 	    x[7]: 'kjdshfg'
	#     }
    #     lst.append(new_dict)
    #     return jsonify(lst)


        

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
