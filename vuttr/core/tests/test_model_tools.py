from django.test import TestCase
from vuttr.core.models import Tools, Tags

class ModelTools(TestCase):
    def setUp(self):
        self.tool = Tools.objects.create(
            title = "Notion",
            link = "https://notion.so",
            description = "All in one tool to organize teams and ideas. Write, plan, collaborate, and get organized.",
        )
        
    def test_model_exists(self):
        self.assertTrue(Tools.objects.exists())

    def test_model_relationship_exists(self):
        self.tool.tags.create(name = 'organization')
        self.tool.tags.create(name = 'planning')
        self.tool.tags.create(name = 'collaboration')
        self.tool.tags.create(name = 'writing')
        self.tool.tags.create(name = 'calendar')

        self.assertTrue(self.tool.tags.exists())
