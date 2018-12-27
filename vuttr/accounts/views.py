from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import json

def login_view(request):
    if request.method == "POST":
        resp = json.loads(request.body)
        user = authenticate(request, username=resp['username'], password=resp['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/tools')
        else:
            data = {"message": "Invalid login credentials"}
            return HttpResponse(json.dumps(data), status=403, content_type="application/json")
    else:
        data = {"message": "To login send a json dictionary containing your username and password"}
        return HttpResponse(json.dumps(data), content_type="application/json")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')

def create_user(request):
    try:
        data = json.loads(request.body)
        User.objects.create_user(username=data['username'], email=data['email'], password=data['password'])
        message = {"message": "User created successfully"}
        return HttpResponse(json.dumps(message), content_type="application/json")
    except KeyError:
        return HttpResponse(status=400)
