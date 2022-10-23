from django.shortcuts import get_object_or_404, render
from .models import Post
from .models import Group

# Create your views here.


def index(request):
    template = 'posts/index.html'
    text = 'Последние обновления на сайте'
    title = 'Главная страница'
# Одна строка вместо тысячи слов на SQL:
# в переменную posts будет сохранена выборка из 10 объектов модели Post,
# отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts' : posts,
        'text' : text,
        'title' : title,
    }
    return render(request, template, context)

def group_list(request, slug):
    template = 'posts/group_list.html'
    # Функция get_object_or_404 получает по заданным критериям объект 
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context) 
