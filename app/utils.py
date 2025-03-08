from mistralai import MistralClient
from django.conf import settings

def moderate_review(text):
    """При вызове функции moderate_review(text) мы получим булево значение:

    True если текст безопасный и подходит для публикации
    False если текст содержит нежелательный контент
    """
    client = MistralClient(api_key=settings.MISTRAL_API_KEY)
    
    response = client.moderate(
        input_text=text,
        categories=[
            "hate", "hate/threatening", "self-harm", "sexual", 
            "sexual/minors", "violence", "violence/graphic"
        ]
    )
    
    return not any(response.results)


def moderate_review_with_details(text):
    """При вызове moderate_review_with_details(text) получим словарь с тремя ключами:

    is_safe: булево значение (True/False) о безопасности контента
    categories: список категорий, в которых найдены нарушения
    raw_response: полный ответ от API с детальными результатами проверки по каждой категории"""

    client = MistralClient(api_key=settings.MISTRAL_API_KEY)
    
    response = client.moderate(
        input_text=text,
        categories=[
            "hate", "hate/threatening", "self-harm", "sexual", 
            "sexual/minors", "violence", "violence/graphic"
        ]
    )
    
    return {
        'is_safe': not any(response.results),
        'categories': [cat for cat, flag in response.results.items() if flag],
        'raw_response': response.results
    }
