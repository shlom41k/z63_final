import self as self
from django.test import TestCase

from courses_app.forms import SchoolCourseApplicationForm
from courses_app.models import SchoolCourse


print(f"Tests in '{__name__}' started")


class TestSchoolCourseApplicationForm(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        SchoolCourse.objects.create(
            name='Python for beginner',
            price='60 BYN',
            number_of_lessons="10",
        )

    school_course = SchoolCourse.objects.get(pk=1)

    valid_form_data = [
        {
            'course': school_course,
            'user_name': "Andry22",
            'phone': "+3544564564",
            'telegram': "@shlom41k",
        },
        {   # without telegram
            'course': school_course,
            'user_name': "Andry22",
            'phone': "+3544564564",
        },
    ]

    # Testing all valid data inputs
    def test_valid_data(self):
        for data in self.valid_form_data:
            form = SchoolCourseApplicationForm(data=data)
            self.assertTrue(form.is_valid())

    invalid_form_data = [
        {   # without phone
            'course': school_course,
            'user_name': "Andry22",
            'telegram': "@shlom41k",
        },
        {   # without user_name
            'course': school_course,
            'phone': "+3544564564",
            'telegram': "@shlom41k",
        },
        {  # without course
            'user_name': "Andry22",
            'phone': "+3544564564",
            'telegram': "@shlom41k",
        },
        {  # empty course field
            'course': "",
            'user_name': "Andry22",
            'phone': "+3544564564",
            'telegram': "@shlom41k",
        },
        {  # another type of course field [int]
            'course': 5,
            'user_name': "Andry22",
            'phone': "+3544564564",
            'telegram': "@shlom41k",
        },
        {  # another type of course field [bool]
            'course': False,
            'user_name': "Andry22",
            'phone': "+3544564564",
            'telegram': "@shlom41k",
        },
        {   # empty user_name field
            'course': school_course,
            'user_name': "",
            'phone': "+3544564564",
            'telegram': "@shlom41k",
        },
        {   # empty phone field
            'course': school_course,
            'user_name': "Andry22",
            'phone': "",
            'telegram': "@shlom41k",
        },
    ]

    # Testing all valid data inputs
    def test_invalid_data(self):
        for data in self.invalid_form_data:
            form = SchoolCourseApplicationForm(data=data)
            self.assertFalse(form.is_valid())

    # Test some fields
    test_true_fields = {
        # "field": ("label", ),
        "user_name": ("Person", ),
        "phone": ("Person Phone", ),
        "telegram": ("Telegram", ),
        "course": ("Course", ),
    }

    def test_form_name_field_label(self):
        form = SchoolCourseApplicationForm()

        for field, (label, ) in self.test_true_fields.items():
            self.assertEqual(form.fields[field].label, label)


print(f"Tests in '{__name__}' finished")
