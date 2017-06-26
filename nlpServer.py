import spacy
from flask import Flask
from flask import request
app = Flask(__name__)
nlp = spacy.load('en')

searchphrase = "Car manufacturer"
searchdoc = nlp(searchphrase)

@app.route('/settopic')
def set_topic():
    searchphrase = request.args.get('topic', '')
    searchdoc = nlp(searchphrase)
    print("Searchphrase is: {}".format(searchphrase))
    return searchphrase

@app.route('/rate_phrase')
def rate_phrase():
    comparephrase = request.args.get('phrase', '')
    comparedoc = nlp(comparephrase)
    similarity = str(searchdoc.similarity(comparedoc))
    return similarity
