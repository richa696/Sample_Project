from django.urls import path
from .views import GetCryptoCurrencyList, SaveOrUpdateData
urlpatterns = [
    path('saveorupdate/',SaveOrUpdateData.as_view()),
    path('getData',GetCryptoCurrencyList.as_view())
]