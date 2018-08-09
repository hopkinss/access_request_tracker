from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms
from django.forms import modelformset_factory
from django.shortcuts import render,redirect
from trackapp.models import *
from django.utils import timezone

from trackapp.forms import CS096Form

def main_view(request):
    if request.method=="POST":
        form=CS096Form(request.POST)
        if form.is_valid():
            model_instance=form.save(commit=False)
            model_instance.timestamp= timezone.now()
            model_instance.save()
            return redirect('/')
    else:
        form=CS096Form()
        return render(request,'index.html',{'form':form})


from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Protocol,Product,CS096

class PersonListView(ListView):
    model = CS096
    template_name = 'index.html'
    context_object_name = 'people'

class PersonCreateView(CreateView):
    model = CS096
    form_class = CS096Form
    template_name = 'index.html'


    success_url = reverse_lazy('person_changelist')

class PersonUpdateView(UpdateView):
    model = CS096
    form_class = CS096Form
    success_url = reverse_lazy('person_changelist')

def load_protocols(request):
    id = request.GET.get('protocols')

    # protocols = Protocol.objects.filter(product_id=id).order_by('protocol')
    protocols=Protocol.objects.filter(product_id=id)
    return render(request, 'dropdown.html', {'protocols': protocols})

#
# def main_view(request, *args, **kwargs):
#     if request.method=="POST":
#         test = request.POST.get('your_name')
#         context={'name':test}
#         return render(request, 'list.html', context)
#     else:
#         context = {'data': "GET", }
#         return render(request, 'index.html', context)


