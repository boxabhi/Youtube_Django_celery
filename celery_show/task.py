from celery import shared_task
from time import sleep

from django.core.mail import send_mail
from docx2pdf import convert
from django.core.files.storage import FileSystemStorage
import os


@shared_task
def sleepy(duariton):
    sleep(duariton)
    return None



@shared_task
def send_mail_task():
    send_mail('CELERY WORKED YEAH', "CELERY IS COOL" ,
              "cricketacademyofpathanslucknow@gmail.com",   
              ['abhijeetg40@gmail.com'],
              fail_silently = False
              )
    print("MAIL FROM CELERY")
    return None



@shared_task
def convert_doc_to_pdf(myfile):
    sleep(10)
    convert('hotels/static/' + myfile)
    return None
    