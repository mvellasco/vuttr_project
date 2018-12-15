from django.test import TestCase
from vuttr.core.models import Tools, Tags
from vuttr.tools_api.helpers.serializer import serialize



class ToolsViewValidGet(TestCase):
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

    def test_response(self):
        """ GET /tools/ should return all tools """
        data = serialize(Tools.objects.all())
        self.assertContains(self.resp, data)

    def test_get_tool_by_tag(self):
        resp = self.client.get("/tools/?tag=writing")
        tool = serialize(Tools.objects.filter(tags__name="writing"))
        self.assertContains(resp, tool)

    def test_response_404(self):
        """ Response with 404 if no tool with given tag is found """
        resp = self.client.get("/tools/?tag=not_found/")
        self.assertEqual(404, resp.status_code)

class ToolsViewValidPost(TestCase):
    def setUp(self):
        data = {
            "title": "hotel",
            "link": "https://github.com/typicode/hotel",
            "description": "Local app manager. Start apps within your browser, developer tool with local .localhost domain and https out of the box.",
            "tags": ["node", "organizing", "webapps", "domain", "developer", "https", "proxy"]
        }
        self.resp = self.client.post('/tools/', data, content_type="application/json")

    def test_post(self):
        self.assertTrue(201, self.resp.status_code)

    def test_tool_is_created(self):
        self.assertTrue(Tools.objects.exists())

class ToolsViewValidDelete(TestCase):
    def setUp(self):
        self.tool = Tools.objects.create(
            title = "Notion",
            link = "https://notion.so",
            description = "All in one tool to organize teams and ideas. Write, plan, collaborate, and get organized.",
        )
        url = "/tools/{}/".format(self.tool.id)
        self.resp = self.client.delete(url)

    def test_delete(self):
        self.assertEqual(204, self.resp.status_code)

    def test_object_is_deleted(self):
        self.assertFalse(Tools.objects.exists())

class ToolsViewValidPatch(TestCase):
    def setUp(self):
        self.tool = Tools.objects.create(
            title = "Notion",
            link = "https://notion.so",
            description = "All in one tool to organize teams and ideas. Write, plan, collaborate, and get organized.",
        )
        self.url = "/tools/{}/".format(self.tool.id)
        self.data = {
            "title": "hotel",
            "link": "https://github.com/typicode/hotel",
            "description": "Local app manager. Start apps within your browser, developer tool with local .localhost domain and https out of the box."
        }
        self.resp = self.client.patch(self.url, self.data, content_type="application/json")

    def test_patch(self):
        self.assertEqual(200, self.resp.status_code)

    def test_object_is_updated(self):
        updated_tool = Tools.objects.get(id=self.tool.id)
        for key, value in self.data.items():
            with self.subTest():
                self.assertEqual(value, updated_tool.__getattribute__(key))

class ToolsViewInvalidPatch(TestCase):
    def test_response_404(self):
        resp = self.client.patch('/tools/not_found/')
        self.assertEqual(404, resp.status_code)

    def test_response_400(self):
        tool = Tools.objects.create(
            title = "Notion",
            link = "https://notion.so",
            description = "All in one tool to organize teams and ideas. Write, plan, collaborate, and get organized.",
        )
        url = '/tools/{}/'.format(tool.id)
        data = {}
        resp = self.client.patch(url, data)
        self.assertEqual(400, resp.status_code)
