from django.db import models

from apps.core.models import TimeModel
# Create your models here.


class Pregunta(TimeModel):
	la_pregunta = models.CharField(max_length = 200 )
	

