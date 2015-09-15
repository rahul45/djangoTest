from django.db import models

# Create your models here.
# class Book(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL)
#     name = models.CharField(max_length=200)
#     pages = models.IntegerField()

#     def __unicode__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('books_fbv_user:book_edit', kwargs={'pk': self.pk})
class Employee(models.Model):
	uname=models.CharField(max_length=200)
	empId=models.IntegerField()
	email = models.EmailField(max_length=70,blank=True)
	address=models.CharField(max_length=500)

	def __unicode__(self):
		return self.uname


