from django.shortcuts import  redirect, render

from django.views.decorators.csrf import csrf_protect

from django.contrib import auth

from .forms import UserCreateForm


def logout(request):
    auth.logout(request)
    return redirect("/")


@csrf_protect
def login(request):
    args = dict()
    if request.POST:
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(email=email, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            args['user'] = request.user

            return redirect("/")
        else:
            args['login_error'] = "Такой пользователь не найден"
            return render(request, 'signin.html', args)
    else:
        return render(request, 'signin.html', args)


@csrf_protect
def register(request):
    args = dict()
    args['form'] = UserCreateForm()
    if request.POST:
        newuser_form = UserCreateForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['email'],
                                        password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)

            return redirect('/')

        else:
            args['reg_error'] = 'Error.'
            args['form'] = newuser_form
    return render(request, 'registr.html', args)