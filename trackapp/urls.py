from django.conf.urls import url
from django.urls import path
from trackapp.views import main_view
from . import views

urlpatterns = [
    # url(r'^$',
    #     main_view,
    #     name="index"),
        path('kiml', views.PersonListView.as_view(), name='person_changelist'),
        path('', views.PersonCreateView.as_view(), name='person_add'),
        path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
        path('ajax/load-protocols/', views.load_protocols, name='ajax_load_protocols'),
]