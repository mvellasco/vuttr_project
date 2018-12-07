from django.test import TestCase
from vuttr.core.models import Tools, Tags
from vuttr.api.helpers.serializer import serialize



class ToolsViewGet(TestCase):
    def setUp(self):
        self.tool = Tools.objects.create(
            title = "Notion",
            link = "https://notion.so",
            description = "All in one tool to organize teams and ideas. Write, plan, collaborate, and get organized.",
        )
        self.tool.tags.create(name = 'organization')
        self.tool.tags.create(name = 'planning')
        self.tool.tags.create(name = 'collaboration')
        self.tool.tags.create(name = 'writing')
        self.tool.tags.create(name = 'calendar')

        self.resp = self.client.get('/tools/')

    def test_get_status(self):
        self.assertEqual(200, self.resp.status_code)

    def test_has_correct_response(self):
        data = serialize(Tools.objects.all())
        self.assertContains(self.resp, data)

    def test_get_tool_by_tag(self):
        resp = self.client.get("/tools/?tag=writing")
        tool = serialize(Tools.objects.filter(tags__name="writing"))
        self.assertContains(resp, tool)

    def test_with_fixtures(self):
        self.fail("refatore os testes")

class ToolsViewPost(TestCase):

    def test_post(self):
        data = {
            "title": "hotel",
            "link": "https://github.com/typicode/hotel",
            "description": "Local app manager. Start apps within your browser, developer tool with local .localhost domain and https out of the box.",
            "tags": ["node", "organizing", "webapps", "domain", "developer", "https", "proxy"]
        }
        resp = self.client.post('/tools/', data, content_type="application/json")
        self.assertTrue(Tools.objects.exists())

class ToolsViewDelete(TestCase):
    def setUp(self):
        self.tool = Tools.objects.create(
            title = "Notion",
            link = "https://notion.so",
            description = "All in one tool to organize teams and ideas. Write, plan, collaborate, and get organized.",
        )
        url = "/tools/{}/".format(self.tool.id)
        self.resp = self.client.delete(url)

    def test_delete(self):
        self.assertEqual(200, self.resp.status_code)

    def test_objects_is_deleted(self):
        self.assertFalse(Tools.objects.exists())
