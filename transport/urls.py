from django.urls import path
from . import views


urlpatterns = [
	path('last_coordinates',views.Last_coordinates.as_view(),name='last_coordinates'),

]