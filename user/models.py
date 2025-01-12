from django.db import models


# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=128)
    count = models.IntegerField()
    product_status = models.CharField(max_length=12, choices=(
    ('сломанный', 'сломанный'), ('новый', 'новый'), ('используемый', 'используемый')), default='новый')

    class Meta:
        verbose_name = 'позицию инвентаря'
        verbose_name_plural = 'Инвентарь'

    def __str__(self):
        return f'Наименование: {self.name}. Количество: {self.count}'
