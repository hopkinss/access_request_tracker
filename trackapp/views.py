from django.shortcuts import render,redirect,reverse
from trackapp.models import *
from django import  http
from django.views.generic.edit import FormView,View
from rest_framework import viewsets
from .serializers import ProductSerializer,ProtocolSerializer
from trackapp.forms import CS096Form,UserAddForm
from django.views.generic import ListView, CreateView, UpdateView,DetailView,DeleteView
from django.urls import reverse_lazy
from .models import Protocol,Product,CS096


class CS096ListView(ListView):
    """ List view for parent table CS096"""

    model = CS096
    template_name = 'list.html'
    queryset=CS096.objects.all().order_by('project')
    context_object_name = 'entries'

class CS096CreateView(CreateView):
    """ Model form to handle Create for CS096 """

    model = CS096
    queryset = CS096.objects.all()
    form_class = CS096Form
    template_name = 'index.html'
    success_url = reverse_lazy('entry_list')

    def form_invalid(self, form):
        return http.HttpResponse(form.fields)

class AddUserView(View):
    """ View to manage Create for child table UserAccess """

    def get(self,request,pk):
        """
        Handle GET request returns empty UserAccess form with reference to parent CS096 object
        :param request:
        :param pk: Foreign key for CS096
        :return: UserAccess form
        """
        req=CS096.objects.get(pk=pk)
        form=UserAddForm()
        return render(request, 'adduser.html', {'form': form,'cs096_':req})

    def post(self,request,pk):
        """
        Handle POST request - creates new UserAccess record related to CS096 by PK
        :param request:
        :param pk: FK to CS096
        :return: redirect to list
        """
        form=UserAddForm(request.POST)
        if form.is_valid():

            entity=CS096.objects.get(pk=pk)
            entity.useraccesses.create(username=form.cleaned_data.get("username"),action=form.cleaned_data.get("action"),group=form.cleaned_data.get("group"))
            return redirect('/')


class CS096UpdateView(UpdateView):
    """ Model view updates CS096 records """
    model = CS096
    template_name = 'details.html'
    form_class = CS096Form
    queryset =  CS096.objects.filter()
    success_url = reverse_lazy('entry_list')

class CS096UpdateUserView(UpdateView):
    """ Model view updates UserAccess record """
    model = UserAccess
    template_name = 'user_details.html'
    form_class = UserAddForm
    queryset =  UserAccess.objects.filter()
    success_url = reverse_lazy('entry_list')

def load_protocols(request):
    """ Insert child protocol for selected product into cascading select elements"""
    id = request.GET.get('protocols')
    protocols=Protocol.objects.filter(product_id=id)
    return render(request, 'dropdown.html', {'protocols': protocols})

class CS096DeleteView(DeleteView):
    """ Handle POST to delete a CS096 record"""
    template_name = 'delete.html'
    form_class = CS096Form
    queryset =  CS096.objects.filter()
    success_url = reverse_lazy('entry_list')

    def get(self, *a, **kw):
        """
        Delete a CS096 record
        :param a: WSGI GET request for CS096 record
        :param kw: PK - primary key for CS096 record
        :return:
        """
        return self.delete(*a, **kw)

class CS096DeleteUserView(DeleteView):
    """ Delete a single user from UserAccess"""
    template_name = 'delete_user.html'
    queryset =  UserAccess.objects.filter()
    success_url = reverse_lazy('entry_list')

    def get(self, *a, **kw):
        """
        Delete a UserAcess record
        :param a: WSGI GET request for UserAccess record
        :param kw: PK - primary key for UserAccess record
        :return:
        """
        return self.delete(*a, **kw)


class ProductViewSet(viewsets.ModelViewSet):
    """
    Endpoint that returns all Products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProtocolViewSet(viewsets.ModelViewSet):
    """
    Enpoint that returns protocols by product
    """
    queryset = Protocol
    serializer_class = ProtocolSerializer









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
    # class CS096CreateUserView(CreateView):
    #     model = UserAccess
    #
    #     form_class = UserAddForm
    #     template_name = 'adduser.html'
    #     success_url = reverse_lazy('entry_list')
    #
    #     def form_invalid(self, form):
    #         return http.HttpResponse(form.fields)