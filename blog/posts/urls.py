
from django.urls import path, include
from . import views

urlpatterns = [
    path('helloworld/', views.hello_world),
    path("<int:id>/", views.post, name='post'),
    path("accounts/", include('accounts.urls')),
]