#! /bin/bash
virtualenv -p /usr/local/bin/python3.6 spacyenv
source ./spacyenv/bin/activate
pip install -U spacy
pip install flask
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en_default
