from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

translator = Translator()

class FAQ(models.Model):
    question = models.TextField
    answer = RichTextField()
    
    def get_translation(self, lang='en'):
        cache_key = f'faq_{self.id}_{lang}'
        cached_translation = cache.get(cache_key)

        if cached_translation:
            return cached_translation
        
        translated_text = translator.translate(self.question, dest=lang).text

        cache.set(cache_key, translated_text, timeout= 3000)
        return translated_text
    
    def __str__(self):
        return self.question