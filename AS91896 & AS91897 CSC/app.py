#Python
from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DATA_FILE = 'data.json'

# --- NEW: Helper Functions to read/write JSON ---
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"users": [], "bakeries": [], "items": []}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# --- App Routes ---
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # TODO: Add logic here later to save a new user/bakery to data.json
        pass
    return render_template('signup.html')

@app.route('/bakeries')
def bakeries():
    # NEW: Load data and pass the bakeries list to the HTML
    data = load_data()
    return render_template('bakeries.html', bakeries_list=data['bakeries'])

@app.route('/bakery/<bakery_name>')
def bakery_items(bakery_name):
    # NEW: Load data, find items matching this bakery, and pass them to the HTML
    data = load_data()
    
    # This is a list comprehension (a quick way to filter a list in Python)
    matching_items = [item for item in data['items'] if item['bakery'] == bakery_name]
    
    return render_template('items.html', bakery_name=bakery_name, items_list=matching_items)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # TODO: Add logic here later to handle the final order confirmation
        return "Order Placeholder - logic coming soon!"
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
