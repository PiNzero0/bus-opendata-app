# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('agency/', AgencyListView.as_view(), name='agency-list'),
    path('agency/<int:pk>/', AgencyDetailView.as_view(), name='agency-detail'),
    path('agencyjp/', AgencyjpListView.as_view(), name='agencyjp-list'),
    path('agencyjp/<int:pk>/', AgencyjpDetailView.as_view(), name='agencyjp-detail'),
    path('stops/', get_stops, name='get_stops'),
    path('stops/<int:pk>/', StopsDetailView.as_view(), name='stops-detail'),
    path('routes/', RoutesListView.as_view(), name='routes-list'),
    path('routes/<int:pk>/', RoutesDetailView.as_view(), name='routes-detail'),
    path('route_jp/', Route_jpListView.as_view(), name='route_jp-list'),
    path('route_jp/<int:pk>/', Route_jpDetailView.as_view(), name='route_jp-detail'),
    path('trips/', TripsListView.as_view(), name='trips-list'),
    path('trips/<int:pk>/', TripsDetailView.as_view(), name='trips-detail'),
    path('calendar/', CalendarListView.as_view(), name='calendar-list'),
    path('calendar/<int:pk>/', CalendarDetailView.as_view(), name='calendar-detail'),
    path('calendar_date/', CalendarDateListView.as_view(), name='calendar_date-list'),
    path('calendar_date/<int:pk>/', CalendarDateDetailView.as_view(), name='calendar_date-detail'),
    path('fare_attribute/', FareAttributeListView.as_view(), name='fare_attribute-list'),
    path('fare_attribute/<int:pk>/', FareAttributeDetailView.as_view(), name='fare_attribute-detail'),
    path('fare_rule/', FareRuleListView.as_view(), name='fare_rule-list'),
    path('fare_rule/<int:pk>/', FareRuleDetailView.as_view(), name='fare_rule-detail'),
    path('shape/', ShapeListView.as_view(), name='shape-list'),
    path('shape/<int:pk>/', ShapeDetailView.as_view(), name='shape-detail'),
    path('frequency/', FrequencyListView.as_view(), name='frequency-list'),
    path('frequency/<int:pk>/', FrequencyDetailView.as_view(), name='frequency-detail'),
    path('transfer/', TransferListView.as_view(), name='transfer-list'),
    path('transfer/<int:pk>/', TransferDetailView.as_view(), name='transfer-detail'),
    path('translation/', TranslationListView.as_view(), name='translation-list'),
    path('translation/<int:pk>/', TranslationDetailView.as_view(), name='translation-detail'),
    path('feed_info/', FeedInfoListView.as_view(), name='feed_info-list'),
    path('feed_info/<int:pk>/', FeedInfoDetailView.as_view(), name='feed_info-detail'),
    
]