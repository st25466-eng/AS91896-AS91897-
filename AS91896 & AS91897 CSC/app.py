from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)
DATA_FILE = 'data.json'

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
    # TODO: Add logic here later to read bakeries from data.json and pass to template
    return render_template('bakeries.html')

@app.route('/bakery/<bakery_name>')
def bakery_items(bakery_name):
    # TODO: Add logic here later to filter items for this specific bakery
    return render_template('items.html', bakery_name=bakery_name)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # TODO: Add logic here later to handle the final order confirmation
        return "Order Placeholder - logic coming soon!"
        
    return render_template('checkout.html')
<!-- EVERYTHING IS WORK IN PROGRESS TRYING TO GET THE BASIC STRUCTURE OF THE APP SET UP AND FUNCTIONING -->
if __name__ == '__main__':
    app.run(debug=True)