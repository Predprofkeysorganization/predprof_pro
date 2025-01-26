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


class Plan(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    provider = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'позицию плана'
        verbose_name_plural = 'План инвенторя'


class Application(models.Model):
    id_application = models.IntegerField(primary_key=True, blank=True)
    name_application = models.CharField(max_length=128)
    information = models.CharField(max_length=1000)
    status_application = models.CharField(max_length=12, choices=(
        ('необработана', 'необработана'), ('одобрена', 'одобрена'), ('отклонена', 'отклонена')), default='необработана')

    def __str__(self):
        return f'{self.name_application} {self.information} {self.status_application}'

    class Meta:
        verbose_name = 'заявку'
        verbose_name_plural = 'Заявка'


class ApplicationRepair(models.Model):
    id_application_repair = models.IntegerField(primary_key=True, blank=True)
    name = models.CharField(max_length=128)
    repair_info = models.CharField(max_length=1000)
    status_application = models.CharField(max_length=12, choices=(
        ('необработана', 'необработана'), ('одобрена', 'одобрена'), ('отклонена', 'отклонена')), default='необработана')

    def __str__(self):
        return f'{self.id_application_repair} {self.name} {self.repair_info} {self.status_application}'

    class Meta:
        verbose_name = 'заявку на ремонт или замену'
        verbose_name_plural = 'заявка на ремонт или замену'
