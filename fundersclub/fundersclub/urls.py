from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from api import views as apiviews
import views

# register all model views
router = routers.DefaultRouter()
router.register(r'funds', apiviews.FundViewSet)
router.register(r'companies', apiviews.CompanyViewSet)
router.register(r'llcs', apiviews.LlcViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)), # admin login
    url(r'^api/', include(router.urls)), # api access
    url(r'^api/fundsbycompany/(?P<company>\w{1,50})$', apiviews.funds_by_company),
    url(r'^api/fundsbyllc/(?P<llc>\w{1,50})$', apiviews.funds_by_llc),
    url(r'^$', views.index), # api access
]
