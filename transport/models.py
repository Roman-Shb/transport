from django.db import models


class Subdivision(models.Model):
	name = models.CharField(max_length=100,verbose_name='Наименование')

	def __str__(self):
		return self.name





class Transport(models.Model):
	name = models.CharField(max_length=100,verbose_name='Наименование')
	subdivision = models.ForeignKey(Subdivision,verbose_name='Подразделение',on_delete=models.SET_NULL,null=True)
	mac = models.CharField(max_length=100,verbose_name='MAC устройства')
	last_coordinate_x = models.FloatField(verbose_name='Местонахождение по X',null=True,blank=True)
	last_coordinate_y = models.FloatField(verbose_name='Местонахождение по Y',null=True,blank=True)
	

	def __str__(self):
		return self.name





class GPS_data(models.Model):
	x_coordinate = models.FloatField(verbose_name='Координата Х')
	y_coordinate = models.FloatField(verbose_name='Координата У')
	date = models.DateTimeField(auto_now_add=True,verbose_name='Дата/Время')
	mac = models.CharField(max_length=100,verbose_name='MAC устройства')





class Tracking(models.Model):
	transport = models.ForeignKey(Transport,verbose_name='Транспорт',on_delete=models.CASCADE)
	track = models.TextField(verbose_name='Трекинг',null=True,blank=True)
	date = models.DateField(auto_now_add=True,verbose_name='Дата')

