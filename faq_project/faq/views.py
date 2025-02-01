from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer

@api_view(['GET'])
def get_faqs(request):
    lang = request.query_params.get('lang', 'en')
    faqs = FAQ.objects.all()

    data = []
    for faq in faqs:
        faq_data = {
            'question': faq.get_translation(lang, 'question'),
            'answer': faq.get_translation(lang, 'answer')
        }
        data.append(faq_data)

    return Response(data)
