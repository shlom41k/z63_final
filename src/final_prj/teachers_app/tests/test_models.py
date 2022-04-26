from django.test import TestCase

from teachers_app.models import Teacher
from ckeditor_uploader.fields import RichTextUploadingField

print(f"Tests in '{__name__}' started")


class TeacherModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Teacher.objects.create(
            first_name='Ivan',
            last_name='Ivanov',
            photo='/media/school_teachers/175149214_1239513213134711_6969818602112611813_n.jpg',
            short_description=RichTextUploadingField(),
            detail_info=RichTextUploadingField(),
            slogan="I'm a teacher",
        )

    def test_first_name_label(self):
        teacher = Teacher.objects.get(id=1)
        field_label = teacher._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'First Name')

    def test_last_name_label(self):
        teacher = Teacher.objects.get(id=1)
        field_label = teacher._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'Last Name')

    def test_short_description_label(self):
        teacher = Teacher.objects.get(id=1)
        field_label = teacher._meta.get_field('short_description').verbose_name
        self.assertEquals(field_label, 'Description')

    def test_detail_info_label(self):
        teacher = Teacher.objects.get(id=1)
        field_label = teacher._meta.get_field('detail_info').verbose_name
        self.assertEquals(field_label, 'Detail Info')

    def test_slogan_label(self):
        teacher = Teacher.objects.get(id=1)
        field_label = teacher._meta.get_field('slogan').verbose_name
        self.assertEquals(field_label, 'Slogan')

    def test_first_name_max_length(self):
        teacher = Teacher.objects.get(id=1)
        max_length = teacher._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 50)

    def test_last_name_max_length(self):
        teacher = Teacher.objects.get(id=1)
        max_length = teacher._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_last_name_comma_first_name(self):
        teacher = Teacher.objects.get(id=1)
        expected_object_name = f"{teacher.first_name} {teacher.last_name}"
        self.assertEquals(expected_object_name, str(teacher))

    def test_get_url(self):
        teacher = Teacher.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(teacher.get_url(), f"/teachers/{teacher.slug}/")


print(f"Tests in '{__name__}' finished")