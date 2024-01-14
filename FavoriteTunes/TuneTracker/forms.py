from django import forms

class SongForm(forms.Form):
    title = forms.CharField(max_length=200)
    artist = forms.CharField(max_length=100)