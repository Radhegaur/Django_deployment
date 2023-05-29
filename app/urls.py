from django.urls import path
from .views import index,register,user_login,user_logout, special

app_name = 'app'
urlpatterns = [
    path('index/', index , name='index'),
    path('register/', register , name='register'),
    path('logout/', user_logout , name='logout'),
    path('special/', special , name='special'),
    path('login/', user_login , name='login'),
]