from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(label='message', max_length=1000)
