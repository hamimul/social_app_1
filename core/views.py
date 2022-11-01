from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from django.http import HttpResponse


# Create your views here.
def index(request):
    """
    :param request: home
    :return: homepage
    """
    return render(request, 'index.html')


def signup(request):
    """
    :param request: form
    :return: create model objects for user and profile and save form data
    """
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        print(username, email, password2, password)

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "e-mail already existed")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('signup')
            else:
                """
                    create user object for User model
                    and save data Save the form data to model
                """
                user = User.objects.create_user(username=username, email=email, password=password2)
                user.save()

                """ 
                    TODO:
                    login user and redirect to setting page
                    than creat profile to save profile
                """

                """
                    create a profile object for new user
                    and save
                """

                # get the model with User with username
                user_model = User.objects.get(username=username)
                # create a object for profile for same id and save
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()

                return redirect('signup')
        else:
            messages.info(request, "Password not matching")
            return redirect('signup')
    else:
        return render(request, 'signup.html')
