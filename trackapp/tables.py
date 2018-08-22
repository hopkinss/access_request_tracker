import django_tables2 as tables
from .models import CS096,Protocol,Product,FileShare,UserAccess

class CS096Table(tables.Table):
    class Meta:
        model = CS096
        template_name = 'django_tables2/bootstrap.html'