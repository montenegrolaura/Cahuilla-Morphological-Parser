from flask import Flask, request, jsonify
from flask_cors  import CORS, cross_origin
from logging.config import dictConfig
from src.services import Services
import json

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/parse": {"origins": "http://localhost:5001"}})

services = Services()


@app.route('/')
def doc() -> str:
    return "Welcome to the Cahuilla Morphological Parser!"


@app.route("/parse", methods=["POST"])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def parse_word():
    data = request.get_json()
    if 'word' not in data:
        return jsonify({"error": "No word provided"}), 400
    app.logger.info(f"/parse - Got request: {data}")
    try:
        result = services.parse_word(data['word'])
        response_data = result.to_dict()
        return app.response_class(
            response=json.dumps(response_data, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )
        #return jsonify(result.to_dict(), ensure_ascii=False)
    except Exception as e:
        app.logger.error(f"Error parsing word: {e}")
        return jsonify({"error": str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,  debug=True)