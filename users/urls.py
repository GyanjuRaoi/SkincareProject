from django.urls import path
from .views import *

urlpatterns = [
    path('', landingPage, name='landing_page'),
    path('login/', loginUser, name='login_user' ),
    path('aboutus/', aboutus, name='aboutus_page'),
    path('singup/', singupuser, name='signup_user'),
    path('logout/', logoutUser, name='logout_user'),
    

]
