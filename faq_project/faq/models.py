from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

translator = Translator()

class FAQ(models.Model):
    question = models.TextField(null=True)
    answer = RichTextField()

    def get_translation(self, lang='en', field='question'):
        cache_key = f'faq_{self.id}_{field}_{lang}'
        cached_translation = cache.get(cache_key)

        if cached_translation:
            return cached_translation
        
        if field == 'answer':
            text_to_translate = self.answer
        else:
            text_to_translate = self.question

        try:
            translated_text = translator.translate(text_to_translate, dest=lang).text
        except Exception as e:
            print(f"Translation failed: {e}")
            return text_to_translate

        cache.set(cache_key, translated_text, timeout=3600)
        return translated_text

    def __str__(self):
        return self.question
