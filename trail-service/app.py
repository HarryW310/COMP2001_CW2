from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Trail Service!"})

@app.route('/trails', methods=['GET'])
def get_trails():
    # Example response
    return jsonify([
        {"TrailID": 1, "TrailName": "Plymbridge Circular"},
        {"TrailID": 2, "TrailName": "Dartmoor Adventure"}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)