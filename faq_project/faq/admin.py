from django.contrib import admin
from django.utils.html import format_html, strip_tags
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer_preview')
    list_editable = ('question',)
    list_display_links = ('answer_preview',) 
    search_fields = ('question', 'answer')
    list_filter = ('question',)
    list_per_page = 10
    ordering = ('question',)

    def answer_preview(self, obj):
        """Show a preview of the answer instead of full translated content"""
        # Strip HTML tags for preview and limit length
        preview = strip_tags(obj.answer)[:100]
        return format_html('<span title="{}">{}</span>', obj.answer, preview + '...' if len(preview) >= 100 else preview)
    answer_preview.short_description = 'Answer Preview'

    fields = ('question', 'answer')
    # Removed readonly_fields with translation calls that caused N+1 queries
