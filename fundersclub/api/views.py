from api.models import Fund, Company, Llc
from rest_framework import viewsets
from api.serializers import FundSerializer, CompanySerializer, LlcSerializer


class FundViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Fund.objects.all()
    serializer_class = FundSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class LlcViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Llc.objects.all()
    serializer_class = LlcSerializer
