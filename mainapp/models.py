from django.db import models
from django.shortcuts import reverse





class Post(models.Model):
    title = models.CharField('Sarlavha', max_length=300, db_index=True)
    slug = models.SlugField('Manzil',unique=True, null=True)
    description = models.CharField('Qisqacha malumot', max_length=255, db_index=True)
    image = models.ImageField('Rasm', db_index=True)
   

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug':self.slug})
    
class Application(models.Model):
    client_name = models.CharField('Ismingiz', max_length=255)
    client_phone_number = models.CharField('Telefon nomer', max_length=50)

    def __str__(self):
        return self.client_name
    


