from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() 

class Group(models.Model):
    title = models.CharField (max_length = 20)
    slug = models.SlugField()
    description = models.TextField()
    def __str__(self) -> str:
        return f'Группа - {self.title}'

class Post(models.Model): 
    # Тип: TextField
    text = models.TextField() 
    
    # Тип поля: DateTimeField, для хранения даты и времени;
    # параметр auto_now_add определяет, что в поле будет автоматически
    # подставлено время и дата создания новой записи
    pub_date = models.DateTimeField(auto_now_add=True)

    # Тип: ForeignKey, ссылка на модель User
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    group = models.ForeignKey(
        Group,
        blank=True, 
        null=True,
        on_delete=models.CASCADE
    )

#class Event(models.Model):
#    name = models.CharField(max_length=200)
#    start_at = models.DateTimeField()
#    description = models.TextField()
#    contact = models.EmailField()
#    author = models.ForeignKey(
#        User,
#        on_delete = models.CASCADE,
#        related_name = 'events'
#    )
#    location = models.CharField(max_length=400)
