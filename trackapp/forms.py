from django.forms import ModelForm
from trackapp.models import CS096,FileShare,UserAccess,Product,Protocol,PrivActions,UserActions


class CS096Form(ModelForm):
    class Meta:
        model=CS096
        fields=['project','protocol','ecms_link','requestor','approver']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['protocol'].queryset = Protocol.objects.none()