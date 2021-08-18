from django.db import models

class Form(models.Model):
    first_name=models.CharField(max_length=30, help_text='eg Jane')
    last_name=models.CharField(max_length=30, help_text='eg Doe')
    email=models.EmailField(max_length=30, help_text='eg yourname@gmail.com')
    message=models.CharField(max_length=300, default='Hello')
"""Create a resume page, the page should contain a contact form
Host it on heroku
I am marking the ability of your form to work and the resume page being able to be hosted on heroku
"""

