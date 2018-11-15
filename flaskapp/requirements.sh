#!/bin/bash
# Installing Python requirements for warren
# Requirements: Python 3.x, Pip

echo "Installing pip..."

# Install pip
apt-get install python3-pip

echo "Finished installing pip!"

echo "Installing requirements for warren..."

# Required modules (in alphabetical order)
pip3 install flask
pip3 install jieba
pip3 install mysql-connector-python
pip3 install OpenCC
pip3 install virtualenv

echo "Finished installing requirements!"