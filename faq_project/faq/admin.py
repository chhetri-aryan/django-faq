from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'get_translated_question', 'get_translated_answer')
    list_editable = ('question',)
    list_display_links = ('answer',) 
    search_fields = ('question', 'answer')
    list_filter = ('question',)
    list_per_page = 10
    ordering = ('question',)

    def get_translated_question(self, obj):
        return obj.get_translation(lang='en', field='question')
    get_translated_question.short_description = 'Translated Question'

    def get_translated_answer(self, obj):
        return obj.get_translation(lang='en', field='answer') 
    get_translated_answer.short_description = 'Translated Answer'

    fields = ('question', 'answer')
    readonly_fields = ('get_translated_question', 'get_translated_answer')
