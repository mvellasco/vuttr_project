from django.test import TestCase
from django.contrib.auth.models import User
import json


class LoginViewValid(TestCase):
    def test_post_with_valid_user(self):
        self.user = User.objects.create_user('mvellasco', 'miguelvellasco@gmail.com', '123456')
        resp = self.client.post('/accounts/login', {"username": "mvellasco", "password": "123456"}, content_type="application/json")
        self.assertEqual(302, resp.status_code)

class LoginViewInvalid(TestCase):
    def test_post_with_invalid_user(self):
        credentials = {'username': 'mvellasco', 'password': '123456'}
        resp = self.client.post('/accounts/login', data=credentials, content_type="application/json")
        self.assertEqual(403, resp.status_code)

    def test_has_message_in_post_response(self):
        credentials = {'username': 'mvellasco', 'password': '123456'}
        resp = self.client.post('/accounts/login', data=credentials, content_type="application/json")
        data = json.loads(resp.content)
        self.assertEqual(data['message'], "Invalid login credentials")

    def test_has_message_in_get_response(self):
        resp = self.client.get('/tools', follow=True)
        data = json.loads(resp.content)
        self.assertEqual(data['message'], "To login send a json dictionary containing your username and password")
