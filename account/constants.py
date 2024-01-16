#Email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_user_email(subject, confirm_link, template, email_address):
    body = render_to_string(template,{'confirm_link': confirm_link})
    send_email = EmailMultiAlternatives(subject, '', to=[email_address])
    send_email.attach_alternative(body, 'text/html')
    send_email.send()

BLOOD_TYPE = [
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    ]

RH_FACTOR = [
        ('+', 'Positive'),
        ('-', 'Negative'),
    ]

GENDER_TYPE = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

BLOOD_GROUP=(
    (1,'A+'),
    (2,'A-'),
    (3,'B+'),
    (4, 'B-'),
    (5, 'AB+'),
    (6, 'AB-'),
    (7, 'O+'),
    (8, 'O-')
)