from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Block, Page, Button, Settings


def index(request):
    blocks = Block.objects.prefetch_related('buttons').all()

    # Получаем первый объект настроек из базы данных
    try:
        settings = Settings.objects.first()
        title = settings.title if settings else ''
        logo = settings.logo.url if settings and settings.logo else ''
    except Settings.DoesNotExist:
        title = ''
        logo = ''

    context = {
        'blocks': blocks,
        'current_time': timezone.now(),
        'setting_title': title,
        'logo': logo
    }

    return render(request, 'terminal/index.html', context)


def page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    context = {
        'page': page,
        'current_time': timezone.now()
    }
    return render(request, 'terminal/page.html', context)


def full_page(request, button_id):
    button = get_object_or_404(Button, pk=button_id)
    context = {
        'button': button,
        'current_time': timezone.now()
    }
    return render(request, 'terminal/full_page.html', context)
