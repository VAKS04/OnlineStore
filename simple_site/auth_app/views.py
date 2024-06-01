from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import *
from django.contrib.auth.views import LoginView


class LoginUser(LoginView):
    form_class = AuthUserForm
    template_name = "auth_app/authForm.html"


    # def get_success_url(self):
    #     return reverse_lazy("index")

def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        # print(form.is_valid())
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('index')
    else:
        form = RegisterUserForm()
    return render(request,'auth_app/registerForm.html',context={"form":form})


def profile(request):
    if request.method == "POST":
        form = UserChangeProfile(data = request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("form:profile")
    else:
        form = UserChangeProfile(instance=request.user)
        # print(request.user.password)
    return render(request,"auth_app/profile.html",context={"form":form})