from django.urls import path
from .views import landing_view
urlpatterns = [
    path('xyz', landing_view, name='landing'),
]
