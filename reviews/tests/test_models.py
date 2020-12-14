from django.contrib.auth.models import User
from django.test import TestCase
from reviews.models import Category

class CategoryModelTest(TestCase):    

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name = 'Terror',color= '#ffffff')
        pass

    def test_color_max_length(self):
        category=Category.objects.get(id=1)
        max_length = Category._meta.get_field('color').max_length
        self.assertEquals(max_length,20)

