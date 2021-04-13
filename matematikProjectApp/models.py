from django.db import models
from ckeditor.fields import RichTextField

class Not(models.Model):
    baslık = models.CharField(max_length=75,verbose_name="Başlık")
    noticerik = RichTextField(blank=False,verbose_name="Notunuz")
    created_date = models.DateTimeField(auto_now_add=True)

    def get_image_or_default(self):
        default3 ='/static/img/ımath.jpg'
        return default3

    def __str__(self):
        return self.baslık

    class Meta:
        verbose_name_plural = "Notlar"
        ordering = ['-created_date']
