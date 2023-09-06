from django.urls import path
from . import views


urlpatterns = [
    path('signup/',views.signup),
    path('signin/',views.signin),
    path('whoami/',views.whoami),
    path('signout/',views.signout),
    path('mypage/<int:id>/',views.mypage),
]