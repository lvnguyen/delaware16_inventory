from config import *
from flask import Flask
import logging
import json

# Start Flask app
app = Flask(__name__)

# Load inventory
with open(INVENTORY_FILE, 'r') as data_file:
	inventory = json.load(data_file)

logging.warning(json.dumps(inventory, sort_keys=True, indent=4))

@app.route('/')
def hello_world():
    return 'Hello, World!'