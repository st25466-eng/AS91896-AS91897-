from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DATA_FILE = 'data.json'

# --- Helper Functions ---
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"users": [], "bakeries": [], "items": []}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# --- Routes ---
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = load_data()
        
        # Grab the info from the HTML form
        account_type = request.form.get('account_type')
        new_account = {
            "name": request.form.get('name'),
            "email": request.form.get('email')
        }
        
        # Save to the correct list in our JSON file
        if account_type == 'bakery':
            data['bakeries'].append(new_account)
        else:
            data['users'].append(new_account)
            
        save_data(data)
        
        # Send them back to the home page after signing up
        return redirect(url_for('home'))
        
    return render_template('signup.html')

@app.route('/bakeries')
def bakeries():
    data = load_data()
    return render_template('bakeries.html', bakeries_list=data['bakeries'])

@app.route('/bakery/<bakery_name>')
def bakery_items(bakery_name):
    data = load_data()
    matching_items = [item for item in data['items'] if item['bakery'] == bakery_name]
    return render_template('items.html', bakery_name=bakery_name, items_list=matching_items)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # 1. If coming from the items page with selected items
        if 'item_names' in request.form:
            data = load_data()
            selected_names = request.form.getlist('item_names')
            
            # Find the full details for the checked items
            selected_items = [item for item in data['items'] if item['name'] in selected_names]
            
            # Calculate the total cost
            total_cost = sum(item['discount_price'] for item in selected_items)
            
            return render_template('checkout.html', selected_items=selected_items, total=total_cost)
            
        # 2. If submitting the final order from the checkout page
        elif 'customer_name' in request.form:
            customer = request.form.get('customer_name')
            return f"<h1>Order Confirmed for {customer}!</h1><p>Thank you for helping reduce food waste. Please pick up your items before closing.</p><a href='/'>Back to Home</a>"
            
    # If someone tries to go to /checkout without selecting items, send them to the bakeries page
    return redirect(url_for('bakeries'))

if __name__ == '__main__':
    app.run(debug=True)
