# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.models import User

from .models import BanTable
from .forms import BanForm

def ban_user(request):
	responsible = request.GET.get('id')
	# responsible = request.user

	form = BanForm(request.POST or None)

	if form.is_valid():
		client_username = request.POST.get('client_username')
		recorded_user = User.objects.get(username=client_username)
		client_email= recorded_user.email
		client_ip = request.META.get('REMOTE_ADDR')
		duration = request.POST.get('duration')

		ban = BanTable(
			client_username = client_username,
			client_email = client_email,
			client_ip = client_ip,
			responsible = responsible,
			duration = duration
		)

		ban.save()

	return render(request,"django_ban/bantool.html",locals())