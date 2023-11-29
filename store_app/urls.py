from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user_information/', UserInformationView.as_view(), name='user_information'),
    path('get_courses/<int:department_id>/', get_courses, name='get_courses'),

]