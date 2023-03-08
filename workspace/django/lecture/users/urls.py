from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'users'
urlpatterns = [
    path("login/", views.login, name='login'),
    path("signup/", views.signup, name='signup'),
    path("signupProcess/", views.signupProcess, name='signupProcess'),
    path("login/", views.login, name='login'),
    path("loginProcess/", views.loginProcess, name='loginProcess'),
    path("logout/", views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
