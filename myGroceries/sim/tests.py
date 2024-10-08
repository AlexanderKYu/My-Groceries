from django.test import TestCase
from django.test import Client

class signInModuleAuthorized(TestCase):
    def setUp(self):
        self.client = Client()
        session = self.client.session
        session['user_data'] = {'given_name': 'TestUser', 'email': 'test@user.com'}
        session.save()

    def test_OAuth_no_redirect(self):
        with self.captureOnCommitCallbacks(execute=True) as callbacks:
            response = self.client.get("/")
        
        self.assertEqual(response.status_code, 200)

