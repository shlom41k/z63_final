from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.views import View

from .forms import FeedBackForm


class FeedBackView(View):
    """
    View for feedback form
    """
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()

        return render(request, 'contacts_app/contacts.html', context={
            'form': form,
            'title': 'Написать нам',
        })

    def post(self, request, *args, **kwargs):
        form = FeedBackForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send email
            try:
                send_mail(f'От {name} | {subject}', message, from_email, ['ZerGey1994MU@mail.ru'])
            except BadHeaderError:
                return HttpResponse('Невалидный заголовок')

            return HttpResponseRedirect('success')

        return render(request, 'contacts_app/contacts.html', context={
            'form': form,
        })


class SuccessView(View):
    """
    View for success page
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts_app/success.html', context={
            'title': 'Спасибо',
        })
