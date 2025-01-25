from django.urls import path
from . import views

urlpatterns = [
    path('blog/<int:blog_id>/', views.blog_detail_page, name='blog_detail'),  # blog_id
    # Boshqa URL'lar...
]
