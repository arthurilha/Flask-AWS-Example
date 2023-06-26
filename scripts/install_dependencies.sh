#!/bin/bash
sudo apt-get update
sudo apt-get install virtualenv python3 python3-pip

cd /home/ubuntu/
virtualenv -ppython3 venv
source venv/bin/activate
pip install -r Flask-AWS-Example/requirements.txt
