from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms
from django.forms import modelformset_factory
from django.shortcuts import render,redirect,reverse
from trackapp.models import *
from django.utils import timezone
from django import  http
from django.views.generic.edit import FormView


from trackapp.forms import CS096Form


from django.views.generic import ListView, CreateView, UpdateView,DetailView,DeleteView
from django.urls import reverse_lazy
from .models import Protocol,Product,CS096


class CS096CreateView(CreateView):
    model = CS096

    # fields=['project','protocol','ecms_link','requestor','approver']
    form_class = CS096Form
    template_name = 'index.html'
    success_url = reverse_lazy('entry_list')

    def form_invalid(self, form):
        return http.HttpResponse(form.fields)


class CS096ListView(ListView):
    model = CS096
    template_name = 'list.html'
    queryset = CS096.objects.all()
    context_object_name = 'entries'

class CS096UpdateView(UpdateView):
    model = CS096
    template_name = 'details.html'
    form_class = CS096Form
    queryset =  CS096.objects.filter()
    success_url = reverse_lazy('entry_list')


def load_protocols(request):
    id = request.GET.get('protocols')
    protocols=Protocol.objects.filter(product_id=id)
    return render(request, 'dropdown.html', {'protocols': protocols})

class CS096DeleteView(DeleteView):
    template_name = 'delete.html'
    form_class = CS096Form
    queryset =  CS096.objects.filter()
    success_url = reverse_lazy('entry_list')

    def get(self, *a, **kw):
        return self.delete(*a, **kw)

#
# def main_view(request):
#     if request.method=="POST":
#         form=CS096Form(request.POST)
#         if form.is_valid():
#             model_instance=form.save(commit=False)
#             model_instance.timestamp= timezone.now()
#             model_instance.save()
#             return redirect('/')
#     else:
#         form=CS096Form()
#         return render(request,'index.html',{'form':form})


