from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home

class homeTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found=resolve('/')
        self.assertEqual(found.func,home)

    def test_home_page_return_correct_html(self):
        request=HttpRequest()
        response=home(request)
        content=render_to_string('html/home.html')
        self.assertIn(content,response.content.decode())

    def test_show_items_after_enter_msg(self):
        request=HttpRequest()
        request.method='post'
        request.POST['item_text']='A new list item'

        response=home(request)
        self.assertIn('A new list item',response.content.decode())
        expect_html=render_to_string(
            'html/home.html',
            {'l'}
        )