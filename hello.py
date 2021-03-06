from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def hello_world():
    result = {
        "message": "Hello World"
    }
    return make_response(jsonify(result))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
