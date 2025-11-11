"""
Unit tests for the Shopify Search App
"""

import unittest
import json
from app import app, MOCK_PRODUCTS


class ShopifySearchTestCase(unittest.TestCase):
    """Test cases for the Shopify Search application"""

    def setUp(self):
        """Set up test client"""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_index_page_loads(self):
        """Test that the index page loads successfully"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Shopify Search', response.data)

    def test_search_with_valid_query(self):
        """Test search API with a valid query"""
        response = self.client.get('/api/search?query=shirt')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('products', data)
        self.assertIn('message', data)
        self.assertEqual(len(data['products']), 1)
        self.assertEqual(data['products'][0]['title'], 'Classic T-Shirt')

    def test_search_with_empty_query(self):
        """Test search API with an empty query"""
        response = self.client.get('/api/search?query=')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data['products']), 0)
        self.assertIn('Please enter a search query', data['message'])

    def test_search_no_results(self):
        """Test search API with a query that returns no results"""
        response = self.client.get('/api/search?query=nonexistentproduct123')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data['products']), 0)
        self.assertIn('Found 0 result(s)', data['message'])

    def test_search_multiple_results(self):
        """Test search API with a query that returns multiple results"""
        response = self.client.get('/api/search?query=cotton')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertGreaterEqual(len(data['products']), 2)
        self.assertIn('Found', data['message'])

    def test_search_case_insensitive(self):
        """Test that search is case-insensitive"""
        response1 = self.client.get('/api/search?query=SHIRT')
        response2 = self.client.get('/api/search?query=shirt')
        data1 = json.loads(response1.data)
        data2 = json.loads(response2.data)
        self.assertEqual(len(data1['products']), len(data2['products']))

    def test_search_in_description(self):
        """Test that search works on product descriptions"""
        response = self.client.get('/api/search?query=athletes')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertGreater(len(data['products']), 0)
        # Verify it found the running shoes
        titles = [p['title'] for p in data['products']]
        self.assertIn('Running Shoes', titles)

    def test_mock_products_exist(self):
        """Test that mock products are defined"""
        self.assertIsNotNone(MOCK_PRODUCTS)
        self.assertGreater(len(MOCK_PRODUCTS), 0)
        # Verify product structure
        for product in MOCK_PRODUCTS:
            self.assertIn('id', product)
            self.assertIn('title', product)
            self.assertIn('description', product)
            self.assertIn('price', product)
            self.assertIn('image', product)


if __name__ == '__main__':
    unittest.main()
