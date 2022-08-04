from django.urls import path
from .views import NounFinderAPIView, PastTenseChangeAPIView, FutureTenseChangeAPIView, PresentTenseChangeAPIView


urlpatterns = [
    path('nounfinder', NounFinderAPIView.as_view()),
    path('past_tense_changer', PastTenseChangeAPIView.as_view()),
    path('future_tense_changer', FutureTenseChangeAPIView.as_view()),
    path('present_tense_changer', PresentTenseChangeAPIView.as_view()),
    ]