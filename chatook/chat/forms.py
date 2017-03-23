from django.forms import ModelForm
from .models import Message

class NewMessageForm(ModelForm):
    def __init__(self, *args, **kwargs):
    	super(NewMessageForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Message
        fields = ['text', 'receiver']
