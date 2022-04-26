from django.test import TestCase
from django.urls import reverse, resolve

from teachers_app.models import Teacher
from ckeditor_uploader.fields import RichTextUploadingField
from teachers_app.views import TeachersView, TeacherDetailView

print(f"Tests in '{__name__}' started")


class TeachersUrlTest(TestCase):

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

    def test_teachers_resolves(self):
        url = reverse('teachers')
        self.assertEqual(resolve(url).func.view_class, TeachersView)

    def test_teacher_detail_resolves(self):
        teacher = Teacher.objects.get(id=1)
        url = reverse('teacher_detail', args=[teacher.slug, ])
        self.assertEqual(resolve(url).func.view_class, TeacherDetailView)


print(f"Tests in '{__name__}' finished")
