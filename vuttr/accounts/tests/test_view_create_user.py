from django.test import TestCase
from django.contrib.auth.models import User


class TestViewCreateUserValid(TestCase):
    def setUp(self):
        data = {"username": "mvellasco", "email": "miguelvellasco@gmail.com", "password": "123456"}
        self.resp = self.client.post('/accounts/create_user', data, content_type='application/json')

    def test_post(self):
        self.assertEqual(200, self.resp.status_code)

    def test_user_is_created(self):
        self.assertTrue(User.objects.exists())

class TestViewCreateUserInvalid(TestCase):
    def test_invalid_post_with_missing_fields(self):
        data = {"username": "mvellasco", "email": "miguelvellasco@gmail.com"}
        resp = self.client.post('/accounts/create_user', data, content_type='application/json')
        self.assertEqual(400, resp.status_code)

    def test_invalid_post_with_no_data(self):
        data = {}
        resp = self.client.post('/accounts/create_user', data, content_type='application/json')
        self.assertEqual(400, resp.status_code)

    def test_no_object_is_created(self):
        data = {"username": "mvellasco", "email": "miguelvellasco@gmail.com"}
        resp = self.client.post('/accounts/create_user', data, content_type='application/json')
        self.assertFalse(User.objects.exists())
