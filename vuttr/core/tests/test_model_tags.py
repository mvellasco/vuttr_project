from django.test import TestCase
from django.core.exceptions import ValidationError
from vuttr.core.models import Tags

class ModelTags(TestCase):
    def test_model_exists(self):
        Tags.objects.create(name="cool_thing")
        self.assertTrue(Tags.objects.exists())

    def test_name_is_unique(self):
        Tags.objects.create(name="another_cool_thing")
        duplicated_tag = Tags(name="another_cool_thing")
        self.assertRaises(ValidationError, duplicated_tag.full_clean)
