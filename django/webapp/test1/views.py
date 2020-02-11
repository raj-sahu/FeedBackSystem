from django.shortcuts import render
from django.http import HttpResponse
from test1.forms import UserProfileInfoForm, UserForm,Ratings

from test1.models import Question,UserProfileInfo

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required # login decorator that makes it easier

global curr_user

def index(request):

    if request.method == "POST":
        form = Ratings(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_rated = request.user
            post.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form=Ratings()

    lis =Question.objects.order_by("question_text")

    return render(request,'index.html',{'form': form,"QUESTIONS": lis})

def review(request): 
    lis=Question.objects.all()
    dic={"QUESTIONS":lis}
    return render(request, 'review.html', context=dic)
# Create your views here.

@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

# Note here that inside of our user_logout function, there is no checking if the user is logged in or not
# the beauty of django is that to do so, you just have to use the decorator login_required. AND THAT IS IT! beautiful.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture


            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password) #user is a boolean that tells us if it is authenticated or not
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index')) #if its everything ok with the login and passwrd, you will log in and be redirected to the index page
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE!")
        else:
            print("LOGIN FAILED!")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied!Username: {} and password {}".format(username, password))
    else:
        return render(request,'login.html',{})
