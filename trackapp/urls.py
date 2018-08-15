from django.conf.urls import url
from django.urls import path
# from trackapp.views import main_view
from . import views
from .models import CS096


urlpatterns = [
    # url(r'^$',
    #     main_view,
    #     name="index"),
    #     url(r'^list/', views.CS096ListView.as_view(), name='entry_list'),
        path('', views.CS096ListView.as_view(), name='entry_list'),
        # path('list/', views.CS096ListView.as_view(), name='entry_list'),
        path('add/', views.CS096CreateView.as_view(), name='entry_add'),
        path('details/<int:pk>/',views.CS096UpdateView.as_view(), name='entry_update'),
        # url(r'^details/<int:pk>/', views.CS096UpdateView.as_view(), name='entry_update'),
        path('ajax/load-protocols/', views.load_protocols, name='ajax_load_protocols'),
        path('delete/<int:pk>/',views.CS096DeleteView.as_view(), name='entry_delete'),
]