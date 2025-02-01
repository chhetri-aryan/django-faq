import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import FAQ

@pytest.mark.django_db
def test_faq_translation():
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a high-level Python web framework."
    )
    assert faq.get_translation('hi', 'question') is not None
    assert faq.get_translation('bn', 'answer') is not None

@pytest.mark.django_db
def test_faq_api():
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a high-level Python web framework."
    )
    client = APIClient()
    url = 'http://127.0.0.1:8000/api/faqs/'
    response = client.get(url, {'lang': 'hi'})
    assert response.status_code == status.HTTP_200_OK
    assert 'question' in response.data[0]
