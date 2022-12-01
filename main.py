from flask import Flask, jsonify
from services.censoService import censoService

app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify({'message': 'it is a test'})

@app.route('/generate_report', methods=['GET'])
def generate_report():
    censoService.union_df()

    return jsonify({'message': 'running'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
