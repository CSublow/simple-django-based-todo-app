# from django.test import TestCase
# from django.shortcuts import get_object_or_404
# from .models import Item

# class TestViews(TestCase):
#     def test_get_home_page(self):
#         page = self.client.get('/') # Fake a request to the url passed in as an arg
#         self.assertEqual(page.status_code, 200) # Assert the page status code is 200, which means a successful connection occured
#         self.assertTemplateUsed(page, 'todo_list.html') # Assert that the page that has been gotten is todo_list.html
        
#     # Testing different pages follows a similiar pattern to testing the home page
#     def test_get_add_item_page(self):
#         page = self.client.get('/add')
#         self.assertEqual(page.status_code, 200)
#         self.assertTemplateUsed(page, 'item_form.html')
        
#     def test_get_edit_item_page(self):
#         item = Item(name = 'Create a test')
#         item.save()
#         # You need to create an instance of the item model so that the view gets an actual id from the database
#         page = self.client.get('/edit/{0}'.format(item.id)) # This is trickier. In order to test the edit page you need to pass in the id
#         self.assertEqual(page.status_code, 200)
#         self.assertTemplateUsed(page, 'item_form.html')
        
#     def test_get_edit_page_for_item_that_does_not_exist(self):
#         page = self.client.get('/edit/1')
#         self.assertEqual(page.status_code, 404)
        
#         # Test the Forms
#     def test_post_create_an_item(self):
#         response = self.client.post("/add", {"name": "Create a test"})
#         item = get_object_or_404(Item, pk = 1)
#         self.assertAlmostEqual(item.done, False)
        
#     def test_post_edit_an_item(self):
#         item = Item(name = "Create a test")
#         item.save()
#         id = item.id # In order to edit items you need the id
        
#         response = self.client.post('/edit/{0}'.format(id), {'name': 'A different name'}) # The last arg here is the values we want to pass in to update
#         item = get_object_or_404(Item, pk = id)
        
#         self.assertEqual('A different name', item.name) # Check the value you passed in as the update is now the item.name

#     def test_post_done_an_item(self):
#         item = Item(name = "Create a test")
#         item.save()
#         id = item.id # In order to edit items you need the id
#         # You don't need to create a new item or edit an item here
#         # Although you don't set the done value here, apparantly Django will set it to true when the test is run
#         response = self.client.post('/done/{0}'.format(id)) # Post to the /done url. Pass in the id so Django knows which one to set to done
        
#         item = get_object_or_404(Item, pk = id)
#         self.assertEqual(item.done, True)

"""Code Institute's github source code is below. Using because for some reason you was only getting 97% test coverage for views"""

from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Item


class TestViews(TestCase):

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "todo_list.html")
    
    def test_get_add_item_page(self):
        page = self.client.get("/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")
    
    def test_get_edit_item_page(self):
        item = Item(name="Create a Test")
        item.save()

        page = self.client.get("/edit/{0}".format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")
    
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)
    
    def test_post_create_an_item(self):
        response = self.client.post("/add", {"name": "Create a Test"})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)
    
    def test_post_edit_an_item(self):
        item = Item(name="Create a Test")
        item.save()
        id = item.id

        response = self.client.post("/edit/{0}".format(id), {"name": "A different name"})
        item = get_object_or_404(Item, pk=id)

        self.assertEqual("A different name", item.name)
    
    def test_toggle_status(self):
        item = Item(name="Create a Test")
        item.save()
        id = item.id

        response = self.client.post("/toggle/{0}".format(id))

        item = get_object_or_404(Item, pk=id)
        self.assertEqual(item.done, True)