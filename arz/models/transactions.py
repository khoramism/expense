from signal import default_int_handler
from django.db import models
from django.urls import reverse

class Transaction(models.Model):
	Choices = (
		('برداشت', 'withdrawal'),
		('واریز', 'deposit'),
	)

	reason = models.CharField(max_length=50, null=True, blank=True)
	
	Necessary = models.BooleanField(default=True,  null=True, blank=True)
	
	price = models.PositiveBigIntegerField()

	full_content = models.TextField()

	date  = models.DateField(null=True)
	
	hour = models.TimeField()

	action = models.CharField(choices=Choices,max_length=50, default= 'برداشت')

	baghi = models.PositiveBigIntegerField()


	class Meta:
		ordering = ['-date']
		
	def __str__(self) -> str:
		return self.reason + str(self.price)

	def get_absolute_url(self):
		return reverse('transaction:detail', args=[self.id])

#class Manufactorer(models.Model)


docs = '''
بانك سامان
برداشت مبلغ 400,000 ازخود پرداز
از 842-777-3667983-
مانده 5,690,424
1400/11/3
07:43:28
'''
