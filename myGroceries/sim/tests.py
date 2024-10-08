from django.test import TestCase
from django.test import Client

class signInModuleAuthorized(TestCase):
    def setUp(self):
        self.client = Client()
        session = self.client.session
        session['user_data'] = {'given_name': 'TestUser', 'email': 'test@user.com'}
        session.save()

    def test_OAuth_no_redirect(self):
        response = self.client.get("/")
        
        self.assertEqual(response.status_code, 200)
    

class signInModuleUnAuthorzed(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_OAuth_redirect(self):
        response = self.client.get("/")

        self.assertRedirects(response, expected_url="/sim/", status_code=302)

