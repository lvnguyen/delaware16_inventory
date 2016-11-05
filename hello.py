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

# Show user profile and his/her inventory list
@app.route('/user/<id>')
def show_user_profile(id):
	try:
		uid = int(id)
		return 'User %d' % uid
	except ValueError:
		return 'Some error occurred'

# Show inventory profile
@app.route('/inventory/<id>')
def show_inventory_id(id):
	try:
		iid = int(id)
		return 'Inventory %d' % iid
	except ValueError:
		return 'Some error occurred'

# Create a reservation. Must be an approved user
@app.route('/reserve')
def make_reservation():
	return 'Make a reservation'

@app.route('/show_inventory')
def show_inventory():
	return 'Show inventory'