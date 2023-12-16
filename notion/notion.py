import json

import requests

with open('../config.txt') as config:
    TOKEN = config.readline().strip()

