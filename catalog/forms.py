import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class RenewBookForm(forms.Form):
	renewal_date = forms.DateField(help_text='Enter a date between now nad 4 weeks (default 3).')
	def clean_renewal_date(self):
		date = self.cleaned_date['renewal_date']
		if date < datetime.date.today():
			raise ValidationError(_('Invalid date - renewal in past'))
		if date > datetime.date.today() + datetime.timedelta(weels=4):
			raise ValodationError(_('Invalid date - renewal more than 9 week ahead'))
		return date

