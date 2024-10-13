import hashlib

from django.test import TestCase
from django.test import Client

class familyAuthorized(TestCase):
    def setUp(self):
        self.client = Client()
        session = self.client.session
        session['user_data'] = {'given_name': 'TestUser', 'email': 'test@user.com'}
        session.save()
    
    def test_authorized_no_redirect(self):
        response = self.client.get("/family/")

        self.assertEqual(response.status_code, 200)
    
    def test_generate_unique_family_code(self):
        userEmail = self.client.session['user_data']['email']
        uniqueHash = hashlib.sha256(userEmail.encode("utf-8")).hexdigest()

        response = self.client.get("/family/")

        self.assertEqual(response.context['familyCode'], uniqueHash)
        


class familyUnauthorized(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_unauthorized_redirect(self):
        response = self.client.get("/family/")

        self.assertRedirects(response, expected_url="/sim/", status_code=302)