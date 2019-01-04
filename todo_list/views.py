from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items = List.objects.all
			messages.success(request, ('Item Has Been Added To List'))
			context = {'all_item': all_items}
			return render(request, 'home.html', context)

	else:
		all_items = List.objects.all
		context = {'all_item': all_items}
		return render(request, 'home.html', context)

def about(request):
	voornaam = 'Evert-Jan'; achternaam = 'Lohnstein'
	context = {'first_name': voornaam, 'last_name': achternaam }
	return render(request, 'about.html', context)

def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request, ('Item Has Been deleted!'))
	return redirect('home')

def cross_off(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('home')

def uncross(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('home')

def edit(request, list_id):
	if request.method == 'POST':
		edititem = List.objects.get(pk=list_id)
		form = ListForm(request.POST or None, instance=edititem)

		if form.is_valid():
			form.save()
			messages.success(request, ('Item Has Been Edited to'))
			return redirect('home')

	else:
		edititem = List.objects.get(pk=list_id)
		context = {'edititem': edititem}
		return render(request, 'edit.html', context)

