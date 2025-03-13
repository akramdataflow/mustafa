from django.shortcuts import render

def about_view(request):
    return render(request, 'common/about.html')

def contact_view(request):
    return render(request, 'common/contact.html')