# -*- coding: utf-8 -*-

from django.forms import ModelForm
from .models import BanTable

class BanForm(ModelForm):
	class Meta:
		model = BanTable
		fields = ['client_username','duration']