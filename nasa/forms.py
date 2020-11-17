from django import forms

class NearEarthObjects(forms.Form):
	start_date = forms.DateTimeField()
	end_date = forms.DateTimeField()


class GetLocation(forms.Form):
	latitude = forms.CharField()
	longitude = forms.CharField()



class GetDate(forms.Form):
   date = forms.DateField(widget=forms.widgets.DateInput(format=['%Y-%m-%d'],attrs={'type': 'date'}))