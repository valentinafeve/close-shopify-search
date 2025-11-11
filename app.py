"""
Shopify Search App - Main Application
A Flask application that provides a search interface for products.
"""

from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Mock API for product search - in a real application, this would be replaced with actual Shopify API
MOCK_PRODUCTS = [
    {
        "id": 1,
        "title": "Classic T-Shirt",
        "description": "Comfortable cotton t-shirt in various colors",
        "price": "$19.99",
        "image": "https://via.placeholder.com/300x300/FF6B6B/FFFFFF?text=T-Shirt"
    },
    {
        "id": 2,
        "title": "Denim Jeans",
        "description": "High-quality denim jeans with perfect fit",
        "price": "$49.99",
        "image": "https://via.placeholder.com/300x300/4ECDC4/FFFFFF?text=Jeans"
    },
    {
        "id": 3,
        "title": "Running Shoes",
        "description": "Lightweight running shoes for athletes",
        "price": "$79.99",
        "image": "https://via.placeholder.com/300x300/95E1D3/FFFFFF?text=Shoes"
    },
    {
        "id": 4,
        "title": "Leather Jacket",
        "description": "Premium leather jacket for style",
        "price": "$199.99",
        "image": "https://via.placeholder.com/300x300/F38181/FFFFFF?text=Jacket"
    },
    {
        "id": 5,
        "title": "Cotton Hoodie",
        "description": "Cozy cotton hoodie for casual wear",
        "price": "$39.99",
        "image": "https://via.placeholder.com/300x300/AA96DA/FFFFFF?text=Hoodie"
    },
    {
        "id": 6,
        "title": "Sports Cap",
        "description": "Stylish sports cap with adjustable strap",
        "price": "$14.99",
        "image": "https://via.placeholder.com/300x300/FCBAD3/FFFFFF?text=Cap"
    },
    {
        "id": 7,
        "title": "Backpack",
        "description": "Durable backpack with multiple compartments",
        "price": "$59.99",
        "image": "https://via.placeholder.com/300x300/FFFFD2/333333?text=Backpack"
    },
    {
        "id": 8,
        "title": "Sunglasses",
        "description": "UV protection sunglasses with modern design",
        "price": "$29.99",
        "image": "https://via.placeholder.com/300x300/A8D8EA/FFFFFF?text=Sunglasses"
    }
]


@app.route('/')
def index():
    """Render the main search page."""
    return render_template('index.html')


@app.route('/api/search', methods=['GET'])
def search():
    """
    API endpoint to search for products.
    Accepts a 'query' parameter and returns matching products.
    """
    query = request.args.get('query', '').lower().strip()
    
    if not query:
        return jsonify({'products': [], 'message': 'Please enter a search query'})
    
    # Filter products based on search query
    # In a real application, this would call the Shopify API
    filtered_products = [
        product for product in MOCK_PRODUCTS
        if query in product['title'].lower() or query in product['description'].lower()
    ]
    
    return jsonify({
        'products': filtered_products,
        'message': f'Found {len(filtered_products)} result(s) for "{query}"'
    })


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
