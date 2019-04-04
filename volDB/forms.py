from django import forms
from .models import Category
from .models import Location
from .models import Organization

# TODO: figure out initial values 
class LandingPageForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.order_by('category'), 
                                            required=False, 
                                            initial="Any", 
                                            widget=forms.Select(attrs={'class' : 'form-control'})
                                            )
    location = forms.ModelChoiceField(queryset=Location.objects.all(), 
                                    required=False, 
                                    initial="Georgetown",
                                    widget=forms.Select(attrs={'class' : 'form-control'}))
    # myLocation = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'searchLocation'}), required=False)
    # radius = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

class ResultsPageForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.order_by('category'), 
                                            required=False, 
                                            initial="Any", 
                                            widget=forms.Select(attrs={'class' : 'refine-form'})
                                            )
    # location = forms.ModelChoiceField(queryset=Location.objects.all(), 
    #                                 required=False, 
    #                                 initial="Georgetown",
    #                                 widget=forms.Select(attrs={'class' : 'form-control'}))
    myLocation = forms.CharField(max_length=100, label='Location', widget=forms.TextInput(attrs={'id': 'searchLocation', 'class':'refine-form'}), required=False)
    radius = forms.IntegerField(label='Radius (mi)', widget=forms.TextInput(attrs={'class': 'refine-form'}), required=False)
    # input type="text" class="form-group" name="location" id="searchLocation"
  
