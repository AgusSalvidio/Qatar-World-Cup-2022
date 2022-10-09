from django.urls import path

from AppQatarWC2022.users.views import login_request,sign_up
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',login_request,name='login'),
    path('sign_up/',sign_up,name='sign_up'),
    path('logout/',LogoutView.as_view(template_name='logout.html'),name='logout'), 
]

    