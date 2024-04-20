from django.test import TestCase

class App1Tests(TestCase):
    def test_example(self):
        response = self.client.get('/app1/example/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Example response")