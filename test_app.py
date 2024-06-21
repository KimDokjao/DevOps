import unittest
import json
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn('<h1>Length Unit Converter</h1>', result.data.decode())

    def test_conversion(self):
        request_data = json.dumps({"value": 1, "from_unit": "meters", "to_unit": "kilometers"})
        response = self.app.post('/convert', data=request_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'result': 0.001})

    def test_invalid_unit(self):
        request_data = json.dumps({"value": 1, "from_unit": "invalid_unit", "to_unit": "meters"})
        response = self.app.post('/convert', data=request_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid unit entered. Please try again.'})

    def test_value_error(self):
        request_data = json.dumps({"value": "abc", "from_unit": "meters", "to_unit": "kilometers"})
        response = self.app.post('/convert', data=request_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid input. Please enter a number for the value.'})

if __name__ == '__main__':
    unittest.main()
