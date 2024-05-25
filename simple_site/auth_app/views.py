from django.shortcuts import render,redirect
from .forms import RegisterUserForm
# from django.contrib.auth.views import LoginView
# from django.contrib.auth.forms import AuthenticationForm


# class LoginUser(LoginView):
#     form_class = AuthenticationForm
#     template_name = "auth/baseForm.html"


    # def get_success_url(self):
    #     return reverse_lazy("index")


def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('index')
    else:
        form = RegisterUserForm()
    return render(request,'auth/registerForm.html',context={"form":form})
# Create your views here.
