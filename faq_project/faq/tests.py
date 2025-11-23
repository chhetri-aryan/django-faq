import pytest
from django.urls import reverse
from django.core.cache import cache
from rest_framework import status
from rest_framework.test import APIClient
from .models import FAQ

@pytest.mark.django_db
def test_faq_translation():
    """Test that translation works correctly"""
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a high-level Python web framework."
    )
    assert faq.get_translation('hi', 'question') is not None
    assert faq.get_translation('bn', 'answer') is not None

@pytest.mark.django_db
def test_faq_api():
    """Test FAQ API endpoint"""
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a high-level Python web framework."
    )
    client = APIClient()
    url = reverse('faq-list')
    response = client.get(url, {'lang': 'hi'})
    assert response.status_code == status.HTTP_200_OK
    assert 'question' in response.data[0]

@pytest.mark.django_db
def test_english_translation_optimization():
    """Test that English translation returns original text without API call"""
    faq = FAQ.objects.create(
        question="What is Python?",
        answer="Python is a programming language."
    )
    # English should return original text immediately
    en_question = faq.get_translation('en', 'question')
    en_answer = faq.get_translation('en', 'answer')
    
    assert en_question == "What is Python?"
    assert en_answer == "Python is a programming language."

@pytest.mark.django_db
def test_database_index_exists():
    """Test that database index exists on question field"""
    from django.db import connection
    from django.db.models import Index
    
    # Get model metadata
    faq_model = FAQ._meta
    
    # Check if question field has db_index=True
    question_field = faq_model.get_field('question')
    assert question_field.db_index is True, "question field should have db_index=True"
    
    # Additional verification using connection introspection if SQLite
    if connection.vendor == 'sqlite':
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT sql FROM sqlite_master WHERE type='index' AND tbl_name='faq_faq' AND sql LIKE '%question%';"
            )
            indexes = cursor.fetchall()
            assert len(indexes) > 0, "Database index on 'question' field should exist"

@pytest.mark.django_db 
def test_api_response_includes_id():
    """Test that optimized API includes FAQ id"""
    faq = FAQ.objects.create(
        question="Test Question",
        answer="Test Answer"
    )
    client = APIClient()
    url = reverse('faq-list')
    response = client.get(url, {'lang': 'en'})
    
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0
    assert 'id' in response.data[0]
    assert response.data[0]['id'] == faq.id
