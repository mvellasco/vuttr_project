from django.test import TestCase
from django.contrib.auth.models import User
import json


class LogoutView(TestCase):
    def setUp(self):
        User.objects.create_user('mvellasco', 'miguelvellasco@gmail.com', '123456')

    def test_logout(self):
        self.client.post('/accounts/login', {"username": "mvellasco", "password": "123456"}, content_type="application/json")
        resp = self.client.post('/accounts/logout')
        self.assertEqual(302, resp.status_code)

    def test_logged_out_user_cannot_access_resources(self):
        self.client.post('/accounts/login', {"username": "mvellasco", "password": "123456"}, content_type="application/json")
        self.client.post('/accounts/logout')
        resp = self.client.get('/tools', follow=True)
        data = json.loads(resp.content)
        self.assertEqual(data['message'], "To login send a json dictionary containing your username and password")
