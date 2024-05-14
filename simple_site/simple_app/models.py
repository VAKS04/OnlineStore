import datetime
from django.db import models,connection
from django.urls import reverse
from django.core.validators import MinValueValidator,MaxValueValidator
# Не стандартная либа
from polymorphic.models import PolymorphicModel


class Device(PolymorphicModel):
    model = models.ForeignKey('ModelDevice',on_delete=models.PROTECT,verbose_name="Модель")
    cat = models.ForeignKey('Category',on_delete=models.PROTECT,null=True)
    name = models.CharField(max_length=100,verbose_name='Название')
    slug = models.SlugField(blank=True)
    image = models.ImageField(upload_to="photos/%Y/%m/%d",verbose_name='Изображение')
    year = models.PositiveIntegerField(validators=[MinValueValidator(1990),MaxValueValidator(datetime.date.today().year)],verbose_name="Год выпуска")
    description = models.TextField(max_length=255,blank=True,verbose_name='Описание')

    bluetoth = models.FloatField(validators=[MinValueValidator(3.0),MaxValueValidator(5.5)],default=4.0,verbose_name="Bluetoth")
    price = models.IntegerField(verbose_name="Цена")
    is_published = models.BooleanField(default=True,verbose_name='Опубликовано')

    def short_description(self):
        return f"Год выпуска:{self.year},"

    def general_feature(self):
        return {
            "Название":self.name,
            "Год выпуска":self.year,
            "Bluetooth":self.bluetoth,
            }
            
    def title(self):
        return f"{self.model.name.title()} {self.name}"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        #первым параметром указывается name из path в urls-приложения
        return reverse("product_page",kwargs={'cat_slug':self.cat.slug,'model_slug':self.model.name,'prod_slug':self.slug})

class Phone(Device):
    ram = models.IntegerField()
    memory = models.IntegerField()

    def general_feature(self):
        base_dict = super().general_feature()
        base_dict['ОЗУ'] = self.ram
        base_dict['Память'] = self.memory
        return base_dict

    class Meta:
        verbose_name = "Смартфоны"
        verbose_name_plural = "Смартфоны"
    
class HeadPhone(Device):
    STATUS_CHOICES = [
        ('Closed','Закрытое'),
        ('Open','Открытое'),
        ('Half-open','Полуоткрытое'),
    ]
    acoustic_design = models.CharField(max_length=20,choices=STATUS_CHOICES,verbose_name="Акустическое оформление")
    lower_limit = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)],default=20,verbose_name="Нижняя граница Гц")
    upper_limit = models.IntegerField(validators=[MinValueValidator(20000),MaxValueValidator(50000)],default=20000, verbose_name="Верхняя Граница Гц")
    active_noise_cancellation = models.BooleanField(default=False,verbose_name="Активное шумоподовление")

    def general_feature(self):
        base_dict =  super().general_feature()
        base_dict['Акустическое оформление'] = self.acoustic_design
        base_dict['Нижняя граница Гц'] = self.lower_limit
        base_dict['Верхняя Граница Гц'] = self.upper_limit
        base_dict['Активное шумоподовление'] = self.active_noise_cancellation
        return base_dict

    class Meta:
        verbose_name = "Наушники"
        verbose_name_plural = "Наушники"

class TemplateForLinks(models.Model):
    title = models.CharField(max_length=255)
    #Можно было через SlugField,но я точно не уверен,
    #что это нормальное решение
    url_path = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Menu(TemplateForLinks):
    class Meta:
        verbose_name = "Панель меню"
        verbose_name_plural = "Панель меню"


class ModelDevice(models.Model):
    name = models.CharField(max_length=100,verbose_name="Название модели")
    cat = models.ManyToManyField('Category')

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели "

    def __str__(self):
        return self.name
    
    def get_industries(self):
        return ", ".join([industry.name for industry in self.cat.all()])
    
    #verbose name for function
    get_industries.short_description = "Производит"


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
    #первым параметром указывается name из path в urls-приложения
        return reverse("category",kwargs={'cat_slug':self.slug})


def delete_table(table_name):
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS {};".format(table_name))