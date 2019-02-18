from django.db import models

class Section(models.Model):
	section_name = models.CharField(max_length=200)
	section_slug = models.CharField(max_length=200, default=1)

	class Meta:
		verbose_name_plural = "Section"

	def __str__(self):
		return self.section_name

class Status(models.Model):
	status_name = models.CharField(max_length=200)
	status_slug = models.CharField(max_length=200)

	class Meta:
		verbose_name = "Status"

	def __str__(self):
		return self.status_name

class Movie(models.Model):
	movie_name = models.CharField(max_length=200, unique=True)
	status = models.ForeignKey(Status, default=1, verbose_name='Status', on_delete=models.SET_DEFAULT)
	section = models.ForeignKey(Section, default=1, verbose_name='Section', on_delete=models.SET_DEFAULT)
	season = models.IntegerField(null=True, blank=True)
	series = models.IntegerField(null=True, blank=True)
	release_date = models.DateField()
	viewing_date = models.DateField(null=True, blank=True)
	who_watched = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.movie_name

class Parameters(models.Model):
	section_name = models.CharField(max_length=40, unique=True)
	status_name = models.CharField(max_length=40, unique=True)		