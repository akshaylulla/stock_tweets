from django import forms

class TickerForm(forms.Form):
    ticker = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mr-sm-2',
            'type' : 'search',
            'placeholer':'Search...',
            'aria-label':'Search'
        }
    ))