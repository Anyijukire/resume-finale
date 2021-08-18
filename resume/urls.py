from django.urls import path
from .views import contact, show_messages, show_resume
from django.conf import settings
from django.conf.urls.static import static
urlpatterns= [
    path("contact/", contact, name="contact"),
    path('resume/' , show_resume, name='show_resume'),
    path('messages', show_messages, name='show_messages')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
