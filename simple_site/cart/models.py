from django.db import models
from auth_app.models import User
from simple_app.models import Device

class CartQuerySet(models.QuerySet):
    
    def total_price(self):
        if self:
            return sum(cart.quantity_device_price() for cart in self)
        return 0

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class Cart(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE,blank=True,null=True,verbose_name="Пользователь")
    device = models.ForeignKey(to=Device,on_delete=models.CASCADE,verbose_name="Устройство")
    session_key = models.CharField(max_length=32,null=True,blank=True)
    quantity = models.PositiveSmallIntegerField(default=1,verbose_name="Количество")

    class Meta:
        db_table = "cart"
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    objects = CartQuerySet().as_manager()

    def __str__(self) -> str:
        return f"{self.user.get_username()} | {self.device.name} | {self.quantity}"
    
    def quantity_device_price(self):
        return self.quantity * self.device.price