from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def main():
  return jsonify({'Status': 'Alive'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
