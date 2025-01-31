# faq/tests/test_models.py
import pytest
from faq.models import FAQ

@pytest.mark.django_db
def test_faq_model_translation():
    # Create a sample FAQ
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework for Python.",
        question_hi="डजांगो क्या है?",
        answer_hi="डजांगो पायथन के लिए एक वेब फ्रेमवर्क है।",
        question_bn="ডjango কি?",
        answer_bn="ডjango পাইথনের জন্য একটি ওয়েব ফ্রেমওয়ার্ক।",
    )

    # Test English translation
    assert faq.get_translated_question('en') == "What is Django?"
    assert faq.get_translated_answer('en') == "Django is a web framework for Python."

    # Test Hindi translation
    assert faq.get_translated_question('hi') == "डजांगो क्या है?"
    assert faq.get_translated_answer('hi') == "डजांगो पायथन के लिए एक वेब फ्रेमवर्क है।"

    # Test Bengali translation
    assert faq.get_translated_question('bn') == "ডjango কি?"
    assert faq.get_translated_answer('bn') == "ডjango পাইথনের জন্য একটি ওয়েব ফ্রেমওয়ার্ক।"