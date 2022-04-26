from django.test import TestCase, Client
from django.urls import reverse
from django.http.response import HttpResponseRedirect


class ContactsViewTest(TestCase):

    test_true_data = {
        # "view_name": ("status_code", "template", ),
        "contacts": (200, "contacts_app/contacts.html", ),
        "success": (200, "contacts_app/success.html", ),
    }

    def setUp(self):
        self.client = Client()

    def test_contacts_view(self):

        for view_name, (status_code, template) in self.test_true_data.items():
            response = self.client.get(reverse(view_name))

            self.assertEqual(response.status_code, status_code)
            self.assertTemplateUsed(response, template)

