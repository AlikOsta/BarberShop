from django.db.models.signals import m2m_changed, pre_save, post_save
from django.dispatch import receiver
from .models import Visit, Review
from .telegram_bot import send_telegram_message

import asyncio
from barber.settings import TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID
from .utils import moderate_review



@receiver(m2m_changed, sender=Visit.services.through)
def send_telegram_notification(sender, instance, action, **kwargs):
    """
    Обработчик сигнала m2m_changed для модели Visit.
    Он обрабатывает добавление КАЖДОЙ услуги в запись на консультацию.
    Отправка ОДНОГО сообщения в телеграмм выполняется в первом условии
    http://127.0.0.1:8000/admin/core/visit/5/change/
    """
    if action == 'post_add' and kwargs.get('pk_set'):
        services = [service.name for service in instance.services.all()]
        message = f"""
*Новая запись* 

*Имя:* {instance.name} 
*Телефон:* {instance.phone or 'не указан'} 
*Комментарий:* {instance.comment or 'не указан'}
*Услуги:* {', '.join(services) or 'не указаны'}
*Дата создания:* {instance.created_at}
*Мастер:* {instance.master.first_name} {instance.master.last_name}
*Ссылка на админ-панель:* http://127.0.0.1:8000/admin/app/visit/{instance.id}/change/
-------------------------------------------------------------
"""
        asyncio.run(send_telegram_message(TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID, message))



@receiver(post_save, sender=Review)
def review_post_save(sender, instance, created, **kwargs):
    if created:
        review = instance
        review_text = review.text
        
        if moderate_review(review_text):
            review.status = 1  # Проверено
        else:
            review.status = 2  # Отклонено
            
        review.save()