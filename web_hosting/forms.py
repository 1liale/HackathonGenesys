from django import forms

class RestaurantForm(forms.Form):
   #user_input = forms.CharField(label='Search for questions related to restaurant', max_length=100)
   user_input = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'id':'search', 'name':'search', 'class':'form-control'}))
