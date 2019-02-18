from django.test import TestCase
from .models import Item

class TestItemModel(TestCase):
    def test_done_defaults_to_false(self): # If the user creates a new item without specifying the 'done' property it will automatically be set to false
        item = Item(name = "Create a test")
        item.save()
        
        self.assertEqual(item.name, "Create a test") # Assert that the name of the item you just created is what you actually set as the name
        # You can siplify the commented out line below through the line below that
        # self.assertEqual(item.done, False)
        self.assertFalse(item.done)
        
    def test_can_create_item_with_name_and_done_status(self):
        item = Item(name = "Create a test", done = True) # Create an item with the name of "Create a test" and a checked done status
        item.save() # Save the item
        
        self.assertEqual(item.name, "Create a test")
        self.assertTrue(item.done)
        
    def test_item_as_a_string(self):
        item = Item(name = "Create a test")
        self.assertEqual("Create a test", str(item)) # Assert the string version of item is the same as the name we passed in
        