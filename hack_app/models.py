from django.db import models

# Create your models here.
class Hack(models.Model):
	hack = models.IntegerField("Yoz:")

	class Meta:
		verbose_name = 'Hack'
		verbose_name_plural = 'Hacks'
	
	def __str__(self):
		return f"{self.hack}"