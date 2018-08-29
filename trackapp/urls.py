from django.conf.urls import url,include
from django.urls import path
import django.contrib.auth.views
from . import views
from .models import CS096
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)



urlpatterns = [

        path('', views.CS096ListView.as_view(), name='entry_list'),
        path('add/', views.CS096CreateView.as_view(), name='entry_add'),
        path('user/<int:pk>/', views.AddUserView.as_view(), name='user_add'),
        path('details/<int:pk>/',views.CS096UpdateView.as_view(), name='entry_update'),
        path('ajax/load-protocols/', views.load_protocols, name='ajax_load_protocols'),
        path('delete/<int:pk>/',views.CS096DeleteView.as_view(), name='entry_delete'),
        url(r'^', include(router.urls)),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        path('user_details/<int:pk>/', views.CS096UpdateUserView.as_view(), name='user_update'),
        path('user_delete/<int:pk>/', views.CS096DeleteUserView.as_view(), name='user_delete'),

]