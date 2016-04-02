# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from . import Choices
class BanTable(models.Model):
	'''
	Table which is holding all the bans plus history. Useful to check whether a User is particularly annoying or not.
	'''


	client_username = models.CharField(max_length=64,db_index=True,help_text=_"Banned person's username.")
	client_email = models.EmailField(db_index=True,help_text=_"Banned person's email.")
	client_ip = models.GenericIPAddressField(db_index=True,help_text=_"Banned person's IP.")
	responsible = models.CharField(max_length=64,help_text=_"Person who is responsible for the ban.")
	date = models.DateTimeField(auto_now_add=True=,help_text="When the ban has been set.")
	duration = models.IntegerField(default=Choices.DURATIONS,help_text=_"Ban duration.") # saving the duration in seconds to use datetime.timedelta objects in the views
	expired = models.BooleanField(default=False,help_text="Has ban expired ?")

	def __init__(self):
		return u"%s - %s banned for %s seconds on the %s" % (self.client_username,self.client_ip,self.duration,self.date)

	class Meta:
		ordering = ['date']
		verbose_name='Ban'
		verbose_name_plural = 'Bans'