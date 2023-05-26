from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Service(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название услуги")
    description = models.TextField(max_length=100, verbose_name="Описание")
    price_from = models.IntegerField(verbose_name="Цена от")
    price_to = models.IntegerField(verbose_name="Цена до")
    img = models.ImageField(upload_to='marketing_site/images/', verbose_name="Изображение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название проекта")
    description = models.TextField(max_length=100, verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена")
    img = models.ImageField(upload_to='marketing_site/images/', verbose_name="Изображение")
    project_date = models.DateField(auto_now_add=True, verbose_name="Дата исполнения")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Звонок"
        verbose_name_plural = "Звонки"


class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.CharField(max_length=100, verbose_name="Email")
    budget = models.CharField(max_length=100, verbose_name="Бюджет")
    task = models.TextField(verbose_name="Задача")
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, verbose_name="Статус заказа", default="В обработке", choices=[('В обработке', 'В обработке'), ('В работе', 'В работе'), ('Выполнено', 'Выполнено'),])

    def __str__(self):
        return f'Заказ #{self.pk}'
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="ФИО")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
