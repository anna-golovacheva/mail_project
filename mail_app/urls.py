from django.urls import path

from mail_app.apps import MailAppConfig
from mail_app.views import MailingListView, MailingCreateView, \
    ClientCreateView, ClientUpdateView, ClientDeleteView, MailingUpdateView, \
    MailingDeleteView, ClientListView, MailingDetailView

app_name = MailAppConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='index'),
    path('<int:pk>/', MailingDetailView.as_view(), name='mailing_card'),
    path('create_mailing/', MailingCreateView.as_view(), name='create_mailing'),
    path('update_mailing/<int:pk>/', MailingUpdateView.as_view(), name='update_mailing'),
    path('delete_mailing/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('update_client/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),

    ]