from django.shortcuts import render
from .models import FAQ

def faq_list(request):
    lang = request.GET.get('lang', 'en')
    
    faqs = FAQ.objects.all()
    
    faqs_with_translations = []
    for faq in faqs:
        faqs_with_translations.append({
            'question': faq.get_translated_question(lang),
            'answer': faq.get_translated_answer(lang),
        })
    
    return render(request, 'faq/faq_list.html', {
        'faqs': faqs_with_translations,
        'selected_lang': lang,
    })