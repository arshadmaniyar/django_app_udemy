from django.urls import path
from .views import landing_view, home_view
urlpatterns = [
    path('xyz', landing_view, name='landing'),
    path('home', home_view, name='home'),
]
