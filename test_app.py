import unittest
import json
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_conversion(self):
        request_data = json.dumps({"value": 1, "from_unit": "meters",
                                   "to_unit": "kilometers"})
        response = self.app.post('/convert', data=request_data,
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'result': 0.001})

    def test_invalid_unit(self):
        request_data = json.dumps({"value": 1,
                                   "from_unit": "invalid_unit",
                                   "to_unit": "meters"})
        response = self.app.post('/convert', data=request_data,
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error':
                                         'Invalid unit entered.'})

    def test_value_error(self):
        request_data = json.dumps({"value": "abc",
                                   "from_unit": "meters",
                                   "to_unit": "kilometers"})
        response = self.app.post(
            '/convert', data=request_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json,
                         {'error': 'Invalid input.'})


if __name__ == '__main__':
    unittest.main()
