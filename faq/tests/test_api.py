# faq/tests/test_api.py
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from faq.models import FAQ

@pytest.mark.django_db
def test_faq_api_list():
    # Create a sample FAQ
    FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework for Python.",
    )

    # Test the API endpoint
    client = APIClient()
    url = reverse('api-faq-list')  # Replace with your API endpoint name
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['question'] == "What is Django?"