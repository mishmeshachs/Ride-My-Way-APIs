from flask import Flask, jsonify,request
import unittest
from rides import returnAll
app = Flask(__name__)
class TestRides(unittest.TestCase):
    def test_return(self):
        response = returnAll
        self.assertEqual(response.status_code, 406)

if __name__ == '__main__':
    unittest.main()
