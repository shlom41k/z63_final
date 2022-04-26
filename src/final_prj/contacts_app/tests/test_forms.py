from django.test import TestCase

from contacts_app.forms import FeedBackForm


class TestFeedBackForm(TestCase):

    def test_valid_data(self):
        form = FeedBackForm(data={
            # valid data
            'name': 'Andrew 02',
            'email': "Andry22@mail.ru",
            'subject': "English",
            'message': "Hello world",
        })
        self.assertTrue(form.is_valid())

    invalid_form_data = [
        {   # invalid email
            'name': 'Andrew 02',
            'email': "Andry22",
            'subject': "English",
            'message': "Hello world",
        },
        {    # invalid email
            'name': 'Andrew 02',
            'email': "Andry22@",
            'subject': "English",
            'message': "Hello world",
        },
        {   # invalid email
            'name': 'Andrew 02',
            'email': "Andry22.ru",
            'subject': "English",
            'message': "Hello world",
        },
        {   # empty name field
            'email': "Andry22@mail.ru",
            'subject': "English",
            'message': "Hello world",
        },
        {  # empty email field
            'name': 'Andrew 02',
            'subject': "English",
            'message': "Hello world",
        },
        {  # empty subject field
            'name': 'Andrew 02',
            'email': "Andry22@mail.ru",
            'message': "Hello world",
        },
        {  # empty message field
            'name': 'Andrew 02',
            'email': "Andry22@mail.ru",
            'subject': "English",
        },
        {  # empty message and name fields
            'email': "Andry22@mail.ru",
            'subject': "English",
        },
    ]

    # Testing all invalid data inputs
    def test_invalid_data(self):
        for data in self.invalid_form_data:
            form = FeedBackForm(data=data)
            self.assertFalse(form.is_valid())

    # Test some fields
    test_true_fields = {
        # "field": ("label", ),
        "name": ("Name", ),
        "email": ("Email", ),
        "subject": ("Subject", ),
        "message": ("Message", ),
    }

    def test_form_name_field_label(self):
        form = FeedBackForm()

        for field, (label, ) in self.test_true_fields.items():
            self.assertEqual(form.fields[field].label, label)

