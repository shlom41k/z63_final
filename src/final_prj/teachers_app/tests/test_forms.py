from django.test import TestCase

from teachers_app.models import Teacher
from ckeditor_uploader.fields import RichTextUploadingField
from teachers_app.forms import IndividualLessonApplicationForm


class TestIndividualLessonApplicationForm(TestCase):

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

    def test_form_is_valid(self):
        teacher = Teacher.objects.get(id=1)

        form = IndividualLessonApplicationForm(
            data={
                "teacher": teacher,
                "user_name": "Andrew",
                "phone": "+375251234567",
                "telegram": "https://t.me/Andrew",
            }
        )

        self.assertTrue(form.is_valid())

    def test_form_is_not_valid_without_user_name(self):
        teacher = Teacher.objects.get(id=1)

        form = IndividualLessonApplicationForm(
            data={
                "teacher": teacher,
                "phone": "+375251234567",
                "telegram": "https://t.me/Andrew",
            }
        )

        self.assertFalse(form.is_valid())

    def test_form_is_not_valid_without_teacher(self):
        form = IndividualLessonApplicationForm(
            data={
                "user_name": "Andrew",
                "phone": "+375251234567",
                "telegram": "https://t.me/Andrew",
            }
        )

        self.assertFalse(form.is_valid())

    def test_form_is_not_valid_without_phone(self):
        teacher = Teacher.objects.get(id=1)

        form = IndividualLessonApplicationForm(
            data={
                "teacher": teacher,
                "user_name": "Andrew",
                "telegram": "https://t.me/Andrew",
            }
        )

        self.assertFalse(form.is_valid())

    def test_form_is_valid_without_telegram(self):
        teacher = Teacher.objects.get(id=1)

        form = IndividualLessonApplicationForm(
            data={
                "teacher": teacher,
                "user_name": "Andrew",
                "phone": "+375251234567",
            }
        )

        self.assertTrue(form.is_valid())

    def test_form_user_name_field_label(self):
        form = IndividualLessonApplicationForm()
        self.assertTrue(form.fields['user_name'].label == 'Person')

    def test_form_phone_field_label(self):
        form = IndividualLessonApplicationForm()
        self.assertTrue(form.fields['phone'].label == 'Person Phone')

    def test_form_telegram_field_label(self):
        form = IndividualLessonApplicationForm()
        self.assertTrue(form.fields['telegram'].label == 'Telegram')
