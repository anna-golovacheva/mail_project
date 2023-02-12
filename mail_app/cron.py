from config.settings import EMAIL_HOST_USER
from mail_app.models import Mailing, MailingAttempt
from datetime import datetime, timedelta
from django.core.mail import send_mail


def my_scheduled_job():
    to_send = False
    now = datetime.now()
    mailings = Mailing.objects.filter(status__in=[Mailing.STARTED, Mailing.CREATED])
    for mailing in mailings:
        if mailing.time.strftime("%H:%M") == now.strftime("%H:%M"):
            last_attempt = MailingAttempt.objects.filter(mailing=mailing.id).last()
            from_last = now.date() - last_attempt.time.date()
            if mailing.frequency == Mailing.MONTHLY and from_last == timedelta(days=30) or mailing.frequency == Mailing.WEEKLY and from_last == timedelta(days=7) or mailing.frequency == Mailing.DAILY and from_last == timedelta(days=1):
                to_send = True
        if to_send:
            mailing.status = Mailing.STARTED
            mailing.save()

            try:
                recipients = mailing.recipient.all()
                rec_list = [rec.email for rec in recipients]
                result = send_mail(
                    subject=mailing.message.topic,
                    message=mailing.message.body,
                    from_email=EMAIL_HOST_USER,
                    recipient_list=rec_list,
                    fail_silently=False
                )

                if result:
                    MailingAttempt.objects.create(
                        status=MailingAttempt.SUCCESS,
                        answer=200
                    )
            except Exception as err:
                MailingAttempt.objects.create(
                    status=MailingAttempt.FAIL,
                    answer=err
                )



