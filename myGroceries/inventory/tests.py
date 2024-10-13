from django.test import TestCase
from django.test import Client

class inventoryAuthorized(TestCase):
    def setUp(self):
        self.client = Client()
        session = self.client.session
        session['user_data'] = {'given_name': 'TestUser', 'email': 'test@user.com'}
        session.save()
    
    def test_authorized_no_redirect(self):
        response = self.client.get("/inventory/")

        self.assertEqual(response.status_code, 200)

class inventoryUnauthorized(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_unauthorized_redirect(self):
        response = self.client.get("/inventory/")

        self.assertRedirects(response, expected_url="/sim/", status_code=302)