from django import forms
from .models import Category
from .models import Location
from .models import Organization

class LandingPageForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.order_by('category').exclude(category='.').exclude(category=''), 
                                            required=False, 
                                            widget=forms.Select(attrs={'class' : 'form-control btn btn-light dropdown-toggle',
                                                                'type' : 'button', 'data-toggle' : 'dropdown'}),
                                            initial=0
                                            )
    location = forms.ModelChoiceField(queryset=Location.objects.exclude(location='').exclude(location='.'), 
                                    required=False, 
                                    initial=0,
                                    widget=forms.Select(attrs={'class' : 'form-control btn btn-light dropdown-toggle',
                                                                'type' : 'button', 'data-toggle' : 'dropdown'}))

class ResultsPageForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.order_by('category').exclude(category='.').exclude(category=''), 
                                            required=False, 
                                            initial=0, 
                                            widget=forms.Select(attrs={'class' : 'col-sm-3 form-control btn btn-secondary dropdown-toggle',
                                                                'type' : 'button', 'data-toggle' : 'dropdown'})
                                            )
    location = forms.ModelChoiceField(queryset=Location.objects.exclude(location='').exclude(location='.'), 
                                    required=False, 
                                    initial=0,
                                    widget=forms.Select(attrs={'class' : 'col-sm-3 form-control btn btn-secondary dropdown-toggle',
                                                                'type' : 'button', 'data-toggle' : 'dropdown'}))
    # Uses Google places API and radius field
    # myLocation = forms.CharField(max_length=100, label='Start Location', widget=forms.TextInput(attrs={'id': 'searchLocation', 'class':'col-sm-3'}), required=False)
    # radius = forms.IntegerField(label='Radius', widget=forms.NumberInput(attrs={'class': 'col-sm-1'}), required=False, min_value=0)
  
