import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # CSV-də ID və qiymət string olur, onları çevirmək yaxşı olar
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    products = []
    error = None

    # 1. Source yoxlanışı
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source")

    # 2. ID-yə görə filtrləmə
    if product_id:
        try:
            p_id = int(product_id)
            products = [p for p in products if p['id'] == p_id]
            if not products:
                error = "Product not found"
        except ValueError:
            error = "Product not found"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
