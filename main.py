from flask import Flask, jsonify
from services.censoService import censoService
from environs import Env

app = Flask(__name__)
env = Env()
env.read_env()


@app.route('/')
def hello():
    return jsonify({'message': env.str("version")})


@app.route('/generate_report', methods=['GET'])
def generate_report():
    censoService.union_df()

    return jsonify({'message': 'running'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
