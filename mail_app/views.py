from django.views.generic import ListView, DetailView, CreateView, UpdateView, \
    DeleteView
from django.urls import reverse_lazy, reverse
from mail_app.models import Mailing, Client, MailingAttempt


class MailingListView(ListView):
    model = Mailing


class MailingAttemptListView(ListView):
    model = MailingAttempt
    template_name = 'mail_app/mailing_attempt_list.html'


class MailingDetailView(DetailView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    fields = ('time', 'frequency', 'message', 'recipient')
    success_url = reverse_lazy('mail_app:index')


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ('time', 'frequency')

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('mail_app:update_mailing', kwargs={'pk': pk})


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mail_app:index')


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ('email', 'full_name', 'comments')
    success_url = reverse_lazy('mail_app:clients')


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('email', 'full_name', 'comments')
    success_url = reverse_lazy('mail_app:clients')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mail_app:clients')
