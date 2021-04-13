from django import forms
from .models import Not

class NotForm(forms.ModelForm):
    class Meta:
        model = Not
        fields = ['baslık','noticerik']
    def __init__(self,*args,**kwargs):
        super(NotForm, self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {"class":"form-control"}

