from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer

@api_view(['GET'])
def get_faqs(request):
    lang = request.query_params.get('lang', 'en')
    
    # Try to get all FAQs from cache first (gracefully handle cache failures)
    cache_key = f'faqs_all_{lang}'
    try:
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)
    except Exception:
        # If cache is unavailable, continue without it
        pass
    
    # Use only() to fetch only required fields for better performance
    faqs = FAQ.objects.only('id', 'question', 'answer').all()

    data = []
    for faq in faqs:
        faq_data = {
            'id': faq.id,
            'question': faq.get_translation(lang, 'question'),
            'answer': faq.get_translation(lang, 'answer')
        }
        data.append(faq_data)

    # Cache the complete response for this language (gracefully handle cache failures)
    try:
        cache.set(cache_key, data, timeout=1800)  # 30 minutes cache
    except Exception:
        # If cache is unavailable, continue without it
        pass
    
    return Response(data)
