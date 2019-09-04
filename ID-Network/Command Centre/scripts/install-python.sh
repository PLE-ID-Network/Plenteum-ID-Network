#!/bin/sh

set -eu

# Python tools
sudo apt-get update \
    && sudo apt-get -y upgrade \
    && sudo apt-get install build-essential libssl-dev libffi-dev python-dev python3-pip \
    && printf '\nPython 3 installed successfully\n\n'

pip3 install iroha

printf '\nDepencies are installed successfully!\n\n'