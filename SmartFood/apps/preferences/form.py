from django import forms
from apps.diner.models import Preference

class PreferenceForm(forms.ModelForm):
	class Meta:
		model = Preference
		
		fields={
			'isGlutton',
		}
		
		labels={
			'isGlutton':'are you able to eat a lot of this?',
		}
		
		widgets={
			'isGlutton': forms.BooleanField(required=True),
		}