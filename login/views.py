
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.forms import RegistrationForm
from .forms import (RegistrationForm , EditProfileForm)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import contactForm
# Create your views here.


def about(request):
    context = locals()
    #template = 'about.html'
    form = contactForm(request.POST or None)

    if form.is_valid():
        print( request.POST)
        context = locals()
    return render(request, 'login/about.html',context )
 
def register(request):
    if request.method =='POST':
         form = RegistrationForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             raw_password = form.cleaned_data.get('password1')
             user = authenticate(username=username, password=raw_password)
             login(request, user)
             return redirect( 'home:home' )
    else:
        form = RegistrationForm()
        #form = {'form': form}

        #args = {'form': form}
    return render(request, 'login/reg_form.html',{'form': form} )


#@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    #args = {'user': request.user}
    return render(request,('login/profile.html'), {'user': user})
#@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect( 'login:view_profile' )

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'login/edit_profile.html', args)
#@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST,user=request.user )

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect( 'login:view_profile' )

        else:
            return redirect('/login/change-password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'login/edit_profile.html', args)
#@login_required
def login_admin(request):
    return render(request, 'admin/login.html') 