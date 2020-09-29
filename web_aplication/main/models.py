from django.db import models

class Comments(models.Model):
	login = models.CharField('Имя', max_length=50)
	text = models.TextField('Текст')

	def __str__(self):
		return self.login
