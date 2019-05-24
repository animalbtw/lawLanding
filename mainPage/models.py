from django.db import models

# Create your models here.
class Form(models.Model):
    email = models.EmailField(verbose_name='Почта:')
    phone = models.CharField(max_length=30, verbose_name='Телефон:')

    def __str__(self):
        return 'Песетитель %s %s' % (self.id, self.phone)