from django.test import TestCase
from user.models import User
from django.core.exceptions import ValidationError

class UserValidTests(TestCase):
    def setUp(self):
        User.objects.create(fname = "Test", email = "TestUser@example.com")

    def test_valid_Entry_Creation(self):
        testUser = User.objects.get(email="TestUser@example.com")
        self.assertEqual(testUser.fname, "Test")

class UserInvalidTests(TestCase):

    def test_invalid_email(self):
        invalidUser = User.objects.create(fname = "Test", email = "InvalidEmail")

        self.assertRaises(ValidationError, invalidUser.full_clean)
