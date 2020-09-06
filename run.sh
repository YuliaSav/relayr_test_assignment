#!/bin/sh

# prepare environment
virtualenv venv --python=python3
source venv/bin/activate
pip3 install -r requirements.txt

# run tests
pytest
