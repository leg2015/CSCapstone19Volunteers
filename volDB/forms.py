from django import forms
from .models import Category
from .models import Location
from .models import Organization

# TODO: figure out initial values 
class LandingPageForm(forms.Form):
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.order_by('category'), 
                                            required=False, 
                                            widget=forms.SelectMultiple(attrs={'class' : 'form-control'}),
                                            initial=0
                                            )
    location = forms.ModelChoiceField(queryset=Location.objects.all(), 
                                    required=False, 
                                    initial=0,
                                    widget=forms.Select(attrs={'class' : 'form-control'}))
    # myLocation = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'searchLocation'}), required=False)
    # radius = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

class ResultsPageForm(forms.Form):
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.order_by('category'), 
                                            required=False, 
                                            initial="Any", 
                                            widget=forms.SelectMultiple(attrs={'class' : 'col-sm-3'})
                                            )
    # location = forms.ModelChoiceField(queryset=Location.objects.all(), 
    #                                 required=False, 
    #                                 initial="Georgetown",
    #                                 widget=forms.Select(attrs={'class' : 'form-control'}))
    myLocation = forms.CharField(max_length=100, label='Start Location', widget=forms.TextInput(attrs={'id': 'searchLocation', 'class':'col-sm-3'}), required=False)
    radius = forms.IntegerField(label='Radius', widget=forms.NumberInput(attrs={'class': 'col-sm-1'}), required=False, min_value=0)
    # input type="text" class="form-group" name="location" id="searchLocation"
  
