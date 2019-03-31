from django import forms
from .models import Category
from .models import Location
from .models import Organization

# TODO: figure out initial values 
class LandingPageForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.order_by('category'), 
                                            required=False, 
                                            widget=forms.Select(attrs={'class' : 'form-control'}),
                                            initial=0
                                            )
    location = forms.ModelChoiceField(queryset=Location.objects.all(), 
                                    required=False, 
                                    initial=0,
                                    widget=forms.Select(attrs={'class' : 'form-control'}))
  
