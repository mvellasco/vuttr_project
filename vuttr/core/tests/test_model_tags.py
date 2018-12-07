from django.test import TestCase
from vuttr.core.models import Tags

class ModelTags(TestCase):
    def test_model_exists(self):
        Tags.objects.create(name="cool_thing")

        self.assertTrue(Tags.objects.exists())
