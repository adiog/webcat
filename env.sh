#!/bin/bash

if [[ ! -d venv ]]; then
  virtualenv venv
fi

. $VENV/bin/activate
pip install -r requirements.txt

