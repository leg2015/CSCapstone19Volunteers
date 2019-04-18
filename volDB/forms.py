from django import forms
from .models import Category
from .models import Location
from .models import Organization

class LandingPageForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.order_by('category').exclude(category='.').exclude(category=''), 
                                            required=False, 
                                            widget=forms.Select(attrs={'class' : 'form-control'}),
                                            initial=0
                                            )
    location = forms.ModelChoiceField(queryset=Location.objects.exclude(location='').exclude(location='.'), 
                                    required=False, 
                                    initial=0,
                                    widget=forms.Select(attrs={'class' : 'form-control'}))

class ResultsPageForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.order_by('category').exclude(category='.').exclude(category=''), 
                                            required=False, 
                                            initial=0, 
                                            widget=forms.Select(attrs={'class' : 'col-sm-3'})
                                            )
    myLocation = forms.CharField(max_length=100, label='Start Location', widget=forms.TextInput(attrs={'id': 'searchLocation', 'class':'col-sm-3'}), required=False)
    radius = forms.IntegerField(label='Radius', widget=forms.NumberInput(attrs={'class': 'col-sm-1'}), required=False, min_value=0)
  
