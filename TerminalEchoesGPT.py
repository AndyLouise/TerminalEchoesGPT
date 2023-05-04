from flask import Flask, jsonify, request
from nomic.gpt4all import GPT4All

app = Flask(__name__)
gpt = None

@app.route('/')
def main():
  return jsonify({'Status': 'Alive'})

@app.route('/prompt')
def generate_prompt():
    global gpt
    if gpt is None:
        gpt = GPT4All()
        gpt.open()
    prompt = request.args.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'})
    response = gpt.prompt(prompt)
    return jsonify({'prompt': prompt, 'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
