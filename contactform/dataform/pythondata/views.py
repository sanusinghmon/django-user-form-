from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from pythondata.models import userinsert
from django.contrib import messages




def insertrecord (request):

    if request.method=='POST':
        if request.POST.get('username') and request.POST.get('email'):
            saverecord = userinsert()
            saverecord.username = request.POST.get('username')
            saverecord.email = request.POST.get('email')
            saverecord.save()
            messages.success(request, "Your post has been successfully created")
        return render(request, 'index.html')

    else:
        context = {'error': 'The post was not successfully created. Please enter a title and content'}
        return render(request, 'index.html', context)
