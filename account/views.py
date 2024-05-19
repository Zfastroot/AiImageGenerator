from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model , login ,logout ,authenticate

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password =request.POST.get("password")
        if username and password :
            user = authenticate(request, username = username ,password = password)
            if user:
                login(request , user)
                return redirect('app')
    return render(request , 'account/signin.html')



User = get_user_model()
def signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if username and email and password:  # Check if all required fields are provided
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('app')
    return render(request , 'account/signup.html')


def logout_user(request):
    logout(request)
    return redirect('index')