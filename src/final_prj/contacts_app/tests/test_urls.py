from django.test import TestCase
from django.urls import reverse, resolve

from contacts_app.views import FeedBackView, SuccessView


class ContactsUrlTest(TestCase):

    def test_feedback_url_resolves(self):
        url = reverse('contacts')
        self.assertEquals(resolve(url).func.view_class, FeedBackView)

    def test_success_url_resolves(self):
        url = reverse('success')
        self.assertEquals(resolve(url).func.view_class, SuccessView)
