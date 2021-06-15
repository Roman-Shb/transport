
# Create your views here.
from django.shortcuts import render
from .models import *
from django.views.generic import ListView,CreateView,UpdateView,DetailView
from .filters import *
import json
from django.shortcuts import redirect
import datetime




class Last_coordinates(ListView):
	model = Transport
	template_name = 'transport/last_coordinates.html'
	context_object_name = 'Transports'

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = TransportFilter(self.request.GET,queryset=self.get_queryset())
		return context


