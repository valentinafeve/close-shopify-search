# Shopify Search App

A Flask-based web application that provides a search interface for products. Users can search for products using a search bar, and the app displays matching results from an API.

## Features

- 🔍 Real-time product search
- 🎨 Modern, responsive UI design
- 📱 Mobile-friendly interface
- ⚡ Fast API-based search
- 🛍️ Product cards with images, descriptions, and prices

## Requirements

- Python 3.7+
- Flask 3.0.0
- requests 2.31.0

## Installation

1. Clone the repository:
```bash
git clone https://github.com/valentinafeve/close-shopify-search.git
cd close-shopify-search
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Flask application:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Use the search bar to find products. Try searching for:
   - "shirt"
   - "shoes"
   - "jacket"
   - "hoodie"
   - etc.

## Project Structure

```
close-shopify-search/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css     # Stylesheet
│   └── js/
│       └── app.js        # Frontend JavaScript
└── README.md             # This file
```

## How It Works

1. **Frontend**: User enters a search query in the search bar
2. **API Call**: JavaScript sends the query to `/api/search` endpoint
3. **Backend Processing**: Flask app filters products based on the query
4. **Response**: Matching products are returned as JSON
5. **Display**: Frontend renders product cards with the results

## API Endpoints

### GET `/api/search`

Search for products based on a query parameter.

**Parameters:**
- `query` (string): The search term

**Response:**
```json
{
  "products": [
    {
      "id": 1,
      "title": "Product Name",
      "description": "Product description",
      "price": "$19.99",
      "image": "image_url"
    }
  ],
  "message": "Found X result(s) for 'query'"
}
```

## Customization

### Using Real Shopify API

To connect to a real Shopify store, replace the `MOCK_PRODUCTS` in `app.py` with actual Shopify API calls:

```python
import shopify

# Configure Shopify API
shopify.ShopifyResource.set_site(shop_url)
shopify.ShopifyResource.set_user(api_key)
shopify.ShopifyResource.set_password(password)

# Search products
products = shopify.Product.find(title=query)
```

### Styling

Modify `static/css/style.css` to customize the appearance of the app.

### Adding More Products

Edit the `MOCK_PRODUCTS` list in `app.py` to add more sample products.

## License

MIT License

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.