from api.models import Fund, Company, Llc
from rest_framework import serializers


class FundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fund
        fields = ('bank_account_number', 'companies', 'is_single_asset', 'legal_name', 'llc')

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('display_name')

class LlcSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Llc
        fields = ('created_at', 'dissolved', 'legal_name')
