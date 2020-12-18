from django.core.mail import send_mail

# Create your views here.


def send_mail_without_celery():
    send_mail('CELERY WORKED YEAH', "CELERY IS COOL" ,
              "workwithabhijeetgupta@gmail.com",
              ['abhijeetg40@gmail.com'],
              fail_silently = False
              )
    return None
