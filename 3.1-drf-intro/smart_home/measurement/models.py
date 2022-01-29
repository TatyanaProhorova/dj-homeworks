from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    description = models.TextField(verbose_name='описание')
    name = models.CharField(max_length=255, verbose_name='название')


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements',
                                  verbose_name='id датчика')   # при удалении датчика - измерения удалить
    temperature = models.DecimalField(decimal_places=1, max_digits=4, verbose_name='температура при измерении')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата измерения')
