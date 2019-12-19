from django.shortcuts import render, redirect
from . import models
from . import forms

def index(request):
    return render(request, "phonebook/index.html")


def home(request, number=0):
    return render(request, "phonebook/home.html")


def persons(request):

    person_list = models.Person.objects.all().order_by('last_name')

    person_list_dict = {
        'persons': person_list
    }

    return render(request, "phonebook/person_list.html", person_list_dict)


def person(request, id):
    person = models.Person.objects.get(id=id)
    return render(request, "phonebook/person_detail.html", {'person':person})


def add_person(request):

    if request.method == 'POST':

        form = forms.AddPerson(request.POST)
        if form.is_valid():
            person = models.Person(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                phone_number=form.cleaned_data["phone_number"],
            )
            person.save()
        return redirect('persons')

    else:
        form = forms.AddPerson
        return render(request, "phonebook/add_person.html", {'form': form})

