from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# ตัวอย่างข้อมูลสินค้า
products = [
    {'id': 1, 'name': 'สินค้า A', 'price': 100},
    {'id': 2, 'name': 'สินค้า B', 'price': 150},
    {'id': 3, 'name': 'สินค้า C', 'price': 200},
]

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/buy/<int:product_id>')
def buy(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return f"คุณได้สั่งซื้อ {product['name']} ราคา {product['price']} บาท"
    return "ไม่พบสินค้า"

if __name__ == '__main__':
    app.run(debug=True)
