from django.test import TestCase
from .forms import ItemForm # In order to test the form you're going to first need to import it

# Create your tests here.

class TestToDoItemForm(TestCase):
    
    def test_can_create_an_item_with_just_a_name(self):
        form = ItemForm({'name': 'Create Tests'})
        self.assertTrue(form.is_valid()) # This just checks that form.is_valid() is true
        
    def test_correct_message_for_missing_name(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid()) # Form can not be valid because the value is missing so should assert false
        self.assertEqual(form.errors['name'], [u'This field is required.']) # Assert there is an error in the name with the string 'This field is required'. The '.' is needed at the end else the test will fail as Django will look for an exact match (?)