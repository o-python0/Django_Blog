from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import SnsModel



def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'login.html', {'message': 'アカウントを作成しました！ログインをしてください'})
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このアカウント名は既に使用されています。'})

    return render(request, 'signup.html', {})



def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {'error': 'ログインできませんでした。'})
    return render(request, 'login.html', {})


@login_required
def listfunc(request):
    object_list = SnsModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


@login_required
def detailfunc(request, pk):
    object = get_object_or_404(SnsModel, pk=pk)
    username = request.user.get_username()
    if username not in object.readText:
        object.read = object.read + 1
        object.readText = object.readText + ' ' + username
        object.save()

    return render(request, 'detail.html', {'object': object})


class CreateView(CreateView):
    template_name = 'create.html'
    model = SnsModel
    fields = ('title', 'content', 'author', 'sns_image', 'readText')
    success_url = reverse_lazy('list')



def logoutfunc(request):
    logout(request)
    return redirect('login')



class DeleteView(DeleteView):
    template_name = 'delete.html'
    model = SnsModel
    success_url = reverse_lazy('list')


class UpdateView(UpdateView):
    template_name = 'update.html'
    model = SnsModel
    fields = ('title', 'content', 'sns_image')
    success_url = reverse_lazy('list')

    
def goodfunc(request, pk):
    object = get_object_or_404(SnsModel, pk=pk)
    object.good += 1
    object.save()
    return redirect('list')


def readfunc(request, pk):
    object = get_object_or_404(SnsModel, pk=pk)
    username = request.user.get_username()
    if username in object.readText:
        return redirect('list')
    else:
        object.read = object.read + 1
        object.readText = object.readText + ' ' + username
        object.save()
        return redirect('list')