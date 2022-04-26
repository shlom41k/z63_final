from django.test import TestCase
from django.urls import reverse, resolve

from courses_app.views import SchoolCoursesView, SchoolCourseDetailView
from courses_app.models import SchoolCourse

print(f"Tests in '{__name__}' started")


class CoursesUrlsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        SchoolCourse.objects.create(
            name='Python for beginner',
            price='60 BYN',
            number_of_lessons="10",
        )

    def test_school_courses_url_resolves(self):
        url = reverse('school_courses')
        self.assertEquals(resolve(url).func.view_class, SchoolCoursesView)

    def test_school_course_detail_url_resolves(self):
        school_course = SchoolCourse.objects.get(pk=1)

        url = reverse('school_course_detail', args=[school_course.slug, ])
        self.assertEquals(resolve(url).func.view_class, SchoolCourseDetailView)


print(f"Tests in '{__name__}' finished")
