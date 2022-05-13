from django import views
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('reservation/',views.reservation,name='reservation'),
    path('menu/',views.menu,name='menu'),
    path('gallery/',views.gallery,name='gallery'),
<<<<<<< HEAD
    path('signup_user/',views.signup_user,name='signup_user'),
    path('signin_user/',views.signin_user,name='signin_user'),
    path('signout_user/',views.signout_user,name='signout_user'),
=======
    path('core_body/',views.gallery,name='core_body'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup')
>>>>>>> aebad852be2e87463ef7fb34d56d042c603f1f40
]