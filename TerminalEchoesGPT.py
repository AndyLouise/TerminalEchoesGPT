from flask import Flask, jsonify, request
from nomic.gpt4all import GPT4All

app = Flask(__name__)
m = GPT4All()
m.open()

@app.route('/')
def main():
  return jsonify({'Status': 'Alive'})

@app.route('/prompt')
def generate_prompt():
    prompt = request.args.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'})
    response = m.prompt(prompt)
    return jsonify({'prompt': prompt, 'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
