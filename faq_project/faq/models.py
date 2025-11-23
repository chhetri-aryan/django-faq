from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator
import logging

logger = logging.getLogger(__name__)


class FAQ(models.Model):
    question = models.TextField(null=True, db_index=True)
    answer = RichTextField()

    def get_translation(self, lang='en', field='question'):
        # Return original text for English to avoid unnecessary translation
        if lang == 'en':
            return self.answer if field == 'answer' else self.question
        
        cache_key = f'faq_{self.id}_{field}_{lang}'
        
        # Try to get from cache (gracefully handle cache failures)
        try:
            cached_translation = cache.get(cache_key)
            if cached_translation:
                return cached_translation
        except Exception:
            # If cache is unavailable, continue without it
            pass
        
        text_to_translate = self.answer if field == 'answer' else self.question

        try:
            # Lazy instantiation of translator
            translator = Translator()
            translated_text = translator.translate(text_to_translate, dest=lang).text
        except Exception as e:
            logger.error(f"Translation failed for FAQ {self.id}: {e}")
            return text_to_translate

        # Try to cache the result (gracefully handle cache failures)
        try:
            cache.set(cache_key, translated_text, timeout=3600)
        except Exception:
            # If cache is unavailable, continue without it
            pass
        
        return translated_text

    def __str__(self):
        return self.question or f"FAQ {self.id}"
