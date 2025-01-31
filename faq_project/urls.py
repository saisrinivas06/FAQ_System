from django.contrib import admin
from django.urls import path
from faq.views import faq_list 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faqs/', faq_list, name='faq-list'),  
    path('api/faqs/', faq_list, name='api-faq-list'),  
]