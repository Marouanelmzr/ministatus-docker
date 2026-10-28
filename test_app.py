import unittest
from app import app


class TestMiniStatus(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "ok")

    def test_hello(self):
        response = self.client.get("/hello/Marouane")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "Hello, Marouane!")

    def test_hello_empty_not_found(self):
        response = self.client.get("/hello/")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()