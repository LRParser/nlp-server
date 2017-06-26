#! /bin/bash
virtualenv -p /usr/local/bin/python3.6 spacyenv
source ./spacyenv/bin/activate
pip install -U spacy
pip install flask
python -m spacy download en
python -m spacy link en en_default
