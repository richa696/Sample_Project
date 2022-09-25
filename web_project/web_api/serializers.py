from rest_framework import serializers

from .models import CryptoCurrencyModel

class CryptoCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCurrencyModel
        fields = ['Name','Price','_1h','_24h','_7d','market_cap','volume','circulating_supply']
        