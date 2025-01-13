from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import re
from uchcharaka import transcriber as tr
from uchcharaka import helper

app = Flask(__name__)
CORS(app)

@app.route('/api/public', methods=['POST', 'GET'])
def convert_public():
    #print('There requests are')
    #print(request.json)

    accuracy = True
    preoptions = []
    postoptions = []

    if 'preoptions' in request.values:
        preoptions = request.values['preoptions'].split(',')

    if 'postoptions' in request.values:
        postoptions = request.values['postoptions'].split(',')

    if 'accuracy' not in request.values:
        accuracy = 'Medium'

    if 'source' not in request.values:
        source = 'en-uk'
        preoptions = []
    else:
        source = request.values['source']

    if 'text' in request.values:
        transcriber = tr.Transcriber(request.json['source'], request.json['target'], request.json['accuracy'], request.json['preOptions'], request.json['postOptions'])
        text = transcriber.transcribe(request.json['text'])
    else:
        text = ''

    return text

@app.route('/api/convert', methods=['POST', 'GET'])
def convert_post():
    if 'text' in request.json:
        transcriber = tr.Transcriber(request.json['source'], request.json['target'], request.json['accuracy'], request.json['preOptions'], request.json['postOptions'])
        text = transcriber.transcribe(request.json['text'])
    else:
        text = ''

    text = text.replace('\n', '<br/>')

    return text

@app.route('/api/convertJSON', methods=['POST', 'GET'])
def convert_json():
    transliteration = []

    if 'source' not in request.json.keys():
        return []

    for text in request.json['text']:
        transcriber = tr.Transcriber(request.json['source'], request.json['target'], request.json['accuracy'], request.json['preOptions'], request.json['postOptions'])
        text = transcriber.transcribe(text)
        transliteration.append(text)

    return transliteration

@app.route('/api/convertMap', methods=['POST', 'GET'])
def convert_map():
    if 'source' not in request.json.keys():
        return []

    maps = {}
    for script in helper.IndicScriptsBase:
        maps[script] = {}
        for suffix in helper.suffixes:
            transliteration = []
            for text in request.json['text']:
                transcriber = tr.Transcriber(request.json['source'], script, suffix, request.json['preOptions'], request.json['postOptions'])
                text = transcriber.transcribe(text)
                transliteration.append(text)
            maps[script][suffix]= transliteration
    return maps

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8085, debug=True)
