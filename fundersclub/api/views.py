from django.http import HttpResponse
from api.models import Fund, Company, Llc
from rest_framework import viewsets
from api.serializers import FundSerializer, CompanySerializer, LlcSerializer
import json


class FundViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Fund.objects.select_related('llc').all()
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


def funds_by_company(request, company = ""):
    funds = Fund.objects.all()
    matched_fund_names = ""
    for fund in funds:
        fund_companies = fund.companies.all()
        for fund_company in fund_companies:
            if fund_company.display_name == company:
                matched_fund_names += fund.legal_name + '\n'

    return HttpResponse(matched_fund_names)


def funds_by_llc(request, llc = ""):
    funds = Fund.objects.all()
    matched_fund_names = ""
    for fund in funds:
        if fund.llc.legal_name == llc:
            matched_fund_names += fund.legal_name + "\n"

    return HttpResponse(matched_fund_names)
