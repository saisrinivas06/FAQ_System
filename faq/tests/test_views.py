# faq/tests/test_views.py
import pytest
from django.urls import reverse
from faq.models import FAQ

@pytest.mark.django_db
def test_faq_list_view(client):
    # Create a sample FAQ
    FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework for Python.",
    )

    # Test the view
    url = reverse('faq-list')  # Replace with your URL name
    response = client.get(url)

    assert response.status_code == 200
    assert "What is Django?" in str(response.content)