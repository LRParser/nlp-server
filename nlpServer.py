import spacy
from flask import Flask
from flask import request
from flask import jsonify
from flask import current_app
app = Flask(__name__)
nlp = spacy.load('en_vectors_glove_md')


@app.route('/settopic')
def set_topic():
    current_app.searchphrase = request.args.get('topic', '')
    current_app.searchdoc = nlp(current_app.searchphrase)
    print("Searchphrase is: {}".format(current_app.searchphrase))
    return jsonify(result=current_app.searchphrase)

@app.route('/comparewith')
def compare_with():
    comparephrase = request.args.get('phrase', '')
    comparedoc = nlp(comparephrase)
    similarity = str(current_app.searchdoc.similarity(comparedoc))
    return jsonify(result=similarity, phrase=comparephrase, topic=current_app.searchphrase)
