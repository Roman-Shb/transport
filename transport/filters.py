import django_filters
from .models import *



class TransportFilter(django_filters.FilterSet):
	class Meta:
		model=Transport
		fields = ['subdivision']		



