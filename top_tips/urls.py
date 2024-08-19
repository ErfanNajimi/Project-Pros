from django.urls import path
from .views import TopTipsView

urlpatterns = [
    path('top-tips/', TopTipsView.as_view(), name='top_tips'),
]