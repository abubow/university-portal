from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.index, name='index'),
    path('', views.index, name='index'),
    path('quizes/',views.quizes, name='quizes'),
    path('submissions/',views.submissions, name='submissions'),
    path('material/', views.material, name='material'),
    path('timetable/', views.timetable, name='timetable'),
    path('profile/', views.profile, name='profile'),    
    path('login/', views.login_view, name='login'),
    path('register/', views.signup_view, name='register'),
]