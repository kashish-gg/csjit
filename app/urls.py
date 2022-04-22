
from unicodedata import name
from django.urls import path
from .import views
app_name='app'
urlpatterns=[
    path('',views.index,name='home'),
    path('instructions/',views.instructions,name='instructions'),
    path('topics/',views.topics,name='topics'),
    path('login/', views.loginPage,name='login'),
    path('register/', views.register,name='register'),
    path('submit-paper/', views.submitPaper,name='submitpaper'),
    
# handle routes
    path('handleLogin/', views.handleLogin, name='handleLogin'),
    path('handleRegister/', views.handleRegister, name='handleRegister'),
    path('logout/', views.handleLogout, name='logout'),
]
