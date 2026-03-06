import unittest
import json
from app import app 

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_predict_endpoint(self):
        """Test the predict route returns valid JSON."""
        query = {"country": "all", "year": "2019", "month": "08", "day": "01"}
        response = self.app.post('/predict', 
                                 data=json.dumps(query),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('y_pred', data)

    def test_train_endpoint(self):
        """Test the train route starts successfully."""
        response = self.app.get('/train')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()