from django.shortcuts import render

def index(request):
    print(request.user)
    print(request.user.is_authenticated)
    print(request.user.user_profile.phone)
    return render(request, 'index.html')