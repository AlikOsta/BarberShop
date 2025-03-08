from mistralai import Mistral
from django.conf import settings

def moderate_review(text):
    client = Mistral(api_key=settings.MISTRAL_API_KEY)
    
    response = client.classifiers.moderate_chat(
        model="mistral-moderation-latest",
        inputs=[{"role": "user", "content": text}]
    )
    
    # Get the first result's category scores
    category_scores = response.results[0].category_scores
    
    # Check if any category score is above threshold
    has_violations = any(
        category_score > 0.5 
        for category_score in category_scores.values()
    )
    

    return not has_violations
