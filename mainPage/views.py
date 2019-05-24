from django.shortcuts import render
from .forms import BackForm

# Create your views here.
def home(request):
    form = BackForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
       text = form.cleaned_data
       print(text)

       new_form = form.save()

    return render(request, 'mainPage/index.html', locals()) 