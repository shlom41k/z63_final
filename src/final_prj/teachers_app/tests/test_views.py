from django.test import TestCase, Client
from django.urls import reverse

from teachers_app.models import Teacher
from ckeditor_uploader.fields import RichTextUploadingField


class TeachersViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Teacher.objects.create(
            first_name='Ivan',
            last_name='Ivanov',
            short_description=RichTextUploadingField(),
            detail_info=RichTextUploadingField(),
            slogan="I'm a teacher",
            photo='/media/school_teachers/175149214_1239513213134711_6969818602112611813_n.jpg',
        )

    def setUp(self):
        self.client = Client()

    def test_teachers_view(self):
        response = self.client.get(reverse('teachers'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers_app/teachers.html')

    def test_teachers_detail_view_(self):
        teacher = Teacher.objects.get(id=1)

        response = self.client.get(reverse('teacher_detail', args=[teacher.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers_app/teacher_detail.html')