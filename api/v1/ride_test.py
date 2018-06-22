from flask import Flask, jsonify,request
import unittest
from rides import returnAll
app = Flask(__name__)

class TestRides(unittest.TestCase):
    def test_return(self):
        response = response self.app.(jsonify ({'rides':rides}))
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()