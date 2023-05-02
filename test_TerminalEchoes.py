import json
from unittest import mock
from flask import Flask
from pytest_flask.plugin import JSONResponse

from myapp import app


def test_main():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.json == {'Status': 'Alive'}


@mock.patch('nomic.gpt4all.GPT4All.prompt', return_value='Hello, World!')
def test_generate_prompt(mock_prompt):
    with app.test_client() as client:
        response = client.get('/prompt?prompt=Hello')
        assert response.status_code == 200
        assert response.json == {'prompt': 'Hello', 'response': 'Hello, World!'}

    mock_prompt.assert_called_once_with('Hello')


def test_generate_prompt_no_prompt():
    with app.test_client() as client:
        response = client.get('/prompt')
        assert response.status_code == 200
        assert response.json == {'error': 'No prompt provided'}
