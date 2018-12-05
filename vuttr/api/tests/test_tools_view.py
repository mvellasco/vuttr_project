from django.test import TestCase
import json

class ToolsViewGet(TestCase):
    def test_get_status(self):
        resp = self.client.get('/tools/')
        self.assertEqual(200, resp.status_code)

    def test_has_correct_response(self):
        resp = self.client.get('/tools/')
        data = json.dumps([

            {
                "id": 1,
                "title": "Notion",
                "link": "https://notion.so",
                "description": "All in one tool to organize teams and ideas. Write, plan, collaborate, and get organized. ",
                "tags": [
                    "organization",
                    "planning",
                    "collaboration",
                    "writing",
                    "calendar"
                ]
            },
            {
                "id": 2,
                "title": "json-server",
                "link": "https://github.com/typicode/json-server",
                "description": "Fake REST API based on a json schema. Useful for mocking and creating APIs for front-end devs to consume in coding challenges.",
                "tags": [
                    "api",
                    "json",
                    "schema",
                    "node",
                    "github",
                    "rest"
                ]
            },
            {
                "id": 3,
                "title": "fastify",
                "link": "https://www.fastify.io/",
                "description": "Extremely fast and simple, low-overhead web framework for NodeJS. Supports HTTP2.",
                "tags": [
                    "web",
                    "framework",
                    "node",
                    "http2",
                    "https",
                    "localhost"
                ]
            }
        ])

        self.assertContains(resp, data)
