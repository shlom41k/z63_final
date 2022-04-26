from django.test import TestCase, Client
from django.urls import reverse

from courses_app.models import SchoolCourse

print(f"Tests in '{__name__}' started")


class CoursesViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        SchoolCourse.objects.create(
            name='Python for beginner',
            price='60 BYN',
            number_of_lessons="10",
        )

    test_courses = {
        # "view_name": ("status_code", "template", ),
        "school_courses": (200, "courses_app/courses.html", ),
    }

    test_courses_detail = {
        "school_course_detail": (200, "courses_app/school_course_detail.html",),
    }

    def setUp(self):
        self.client = Client()

    # Test courses page
    def test_courses_view(self):
        for view_name, (status_code, template) in self.test_courses.items():
            response = self.client.get(reverse(view_name))

            self.assertEqual(response.status_code, status_code)
            self.assertTemplateUsed(response, template)

    # Test course detail page
    def test_course_detail_view(self):
        school_course = SchoolCourse.objects.get(pk=1)

        for view_name, (status_code, template) in self.test_courses_detail.items():
            response = self.client.get(reverse(view_name,  args=[school_course.slug]))

            self.assertEqual(response.status_code, status_code)
            self.assertTemplateUsed(response, template)


print(f"Tests in '{__name__}' finished")

