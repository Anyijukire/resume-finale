from django.shortcuts import render
from .forms import ContactForm
from .models import Form
# Create your views here.

# function
def contact(request):
     if request.method == 'POST':
         form=ContactForm(request.POST)
         if form.is_valid():
             form.save()
         else:
             print(form.errors)  
     else:
         form=ContactForm()
     return render(request, 'contact.html', {'form': form}) 

def show_resume(request):
    return render(request, 'resumee.html')                     


def show_messages(request):
    messagess=Form.objects.all()
    return render(request, 'messagess.html', {'messagess': messagess})    