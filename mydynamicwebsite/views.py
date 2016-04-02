from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect

from backend.models import *




class HomePage(View):
    def get(self, request):
        return render(request, 'index.html')

class FoodForm(View):
    def get(self, request):
        allFood = FoodEvent.objects.all()
        context = {'allFood': allFood}
        return render(request, 'foodform.html')

    def post(self, request):
        title = request.POST.get("title")
        name = request.POST.get("name")
        location = request.POST.get("location")
        time = request.POST.get("time")
        organization = request.POST.get("organization")
        new_post = FoodEvent(title=title, name=name, location=location, time=time,
            organization=organization)
        new_post.save()
        return HttpResponseRedirect("/foodform")
        

class FoodList(View):
    def get(self, request):
        context = {}
        context["allFood"] = FoodEvent.objects.all()[::-1]
        return render(request, 'foodlist.html', context)











