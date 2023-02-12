from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, \
    DeleteView
from django.urls import reverse_lazy, reverse

from mail_app.models import Mailing, Client


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    fields = ('time', 'frequency', 'message', 'recipient')
    success_url = reverse_lazy('mail_app:index')


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ('time', 'frequency')
    success_url = reverse_lazy('mail_app:index')


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
