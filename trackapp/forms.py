from django.forms import ModelForm
from trackapp.models import CS096,FileShare,UserAccess,Product,Protocol,PrivActions,UserActions


class CS096Form(ModelForm):
    class Meta:
        model=CS096
        fields=['project','protocol','requestor','approver']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['requestor'].widget.attrs.update({'class': "input-class1"})
        self.fields['approver'].widget.attrs.update({'class': "input-class1"})

class UserAddForm(ModelForm):
    class Meta:
        model=UserAccess
        fields=['username','action','group']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': "input-class1"})
        self.fields['group'].widget.attrs.update({'class': "input-class1"})
