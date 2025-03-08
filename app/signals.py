from django.db.models.signals import m2m_changed, pre_save, post_save
from django.dispatch import receiver
from .models import Visit, Review
from .telegram_bot import send_telegram_message

import asyncio
from barber.settings import TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID
from .utils import moderate_review



@receiver(m2m_changed, sender=Visit.services.through)
def send_telegram_notification(sender, instance, action, **kwargs):
    
    if action == 'post_add' and kwargs.get('pk_set'):
        services = [service.name for service in instance.services.all()]
        message = f"""
*Новая запись* 

*Имя:* {instance.name} 
*Телефон:* {instance.phone or 'не указан'} 
*Комментарий:* {instance.comment or 'не указан'}
*Услуги:* {', '.join(services) or 'не указаны'}
*Дата создания:* {instance.created_at.strftime('%d.%m.%Y %H:%M')}
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
            review.status = 1  
            message = f"""
*Новый отзыв*
*Имя:* {review.author_name}
*Имя мастера:* {review.master.first_name} {review.master.last_name}
*Отзыв:* {review_text}
*Оценка:* {review.rating}/5
*Дата создания:* {instance.created_at.strftime('%d.%m.%Y %H:%M')}
*Ссылка на админ-панель:* http://127.0.0.1:8000/admin/app/review/{review.id}/change/
            """
            asyncio.run(send_telegram_message(TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID, message))
        else:
            review.status = 2  
            
        review.save()