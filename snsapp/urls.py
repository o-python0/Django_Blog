from django.urls import path

from .views import goodfunc, signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, goodfunc, readfunc, CreateView, DeleteView, UpdateView

urlpatterns = [
    path('', loginfunc, name="login"),
    path('signup/', signupfunc, name="signup"),
    path('list/', listfunc, name="list"),
    path('logout/', logoutfunc, name="logout"),
    path('detail/<int:pk>', detailfunc, name="detail"),
    path('create/', CreateView.as_view(), name="create"),
    path('delete/<int:pk>', DeleteView.as_view(), name="delete"),
    path('update/<int:pk>', UpdateView.as_view(), name="update"),
    path('good/<int:pk>', goodfunc, name="good"),
    path('read/<int:pk>', readfunc, name="read"),

]
