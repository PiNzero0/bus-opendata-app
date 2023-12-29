# views.py
from rest_framework import generics
from .models import *
from .serializers import *
from django.shortcuts import render
from django.http import JsonResponse
import asyncio

# modles.pyを参照して、クラスを作成する
class AgencyListView(generics.ListAPIView):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer

class AgencyDetailView(generics.RetrieveAPIView):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer

class AgencyjpListView(generics.ListAPIView):
    queryset = Agencyjp.objects.all()
    serializer_class = AgencyjpSerializer

class AgencyjpDetailView(generics.RetrieveAPIView):
    queryset = Agencyjp.objects.all()
    serializer_class = AgencyjpSerializer

class StopsListView(generics.ListAPIView):
    queryset = Stops.objects.all()
    serializer_class = StopsSerializer

class StopsDetailView(generics.RetrieveAPIView):
    queryset = Stops.objects.all()
    serializer_class = StopsSerializer

class RoutesListView(generics.ListAPIView):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer

class RoutesDetailView(generics.RetrieveAPIView):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer

class Route_jpListView(generics.ListAPIView):
    queryset = Route_jp.objects.all()
    serializer_class = Route_jpSerializer

class Route_jpDetailView(generics.RetrieveAPIView):
    queryset = Route_jp.objects.all()
    serializer_class = Route_jpSerializer

class TripsListView(generics.ListAPIView):
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer

class TripsDetailView(generics.RetrieveAPIView):
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer

class CalendarListView(generics.ListAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

class CalendarDetailView(generics.RetrieveAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

class CalendarDateListView(generics.ListAPIView):
    queryset = Calendar_Dates.objects.all()
    serializer_class = CalendarDateSerializer

class CalendarDateDetailView(generics.RetrieveAPIView):
    queryset = Calendar_Dates.objects.all()
    serializer_class = CalendarDateSerializer

class FareAttributeListView(generics.ListAPIView):
    queryset = Fare_Attributes.objects.all()
    serializer_class = FareAttributeSerializer

class FareAttributeDetailView(generics.RetrieveAPIView):
    queryset = Fare_Attributes.objects.all()
    serializer_class = FareAttributeSerializer

class FareRuleListView(generics.ListAPIView):
    queryset = Fare_Rules.objects.all()
    serializer_class = FareRuleSerializer

class FareRuleDetailView(generics.RetrieveAPIView):
    queryset = Fare_Rules.objects.all()
    serializer_class = FareRuleSerializer

class ShapeListView(generics.ListAPIView):
    queryset = Shapes.objects.all()
    serializer_class = ShapeSerializer 

class ShapeDetailView(generics.RetrieveAPIView):
    queryset = Shapes.objects.all()
    serializer_class = ShapeSerializer

class FrequencyListView(generics.ListAPIView):
    queryset = Frequencies.objects.all()
    serializer_class = FrequencySerializer

class FrequencyDetailView(generics.RetrieveAPIView):
    queryset = Frequencies.objects.all()
    serializer_class = FrequencySerializer

class TransferListView(generics.ListAPIView):
    queryset = Transfers.objects.all()
    serializer_class = TransferSerializer

class TransferDetailView(generics.RetrieveAPIView):
    queryset = Transfers.objects.all()
    serializer_class = TransferSerializer

class TranslationListView(generics.ListAPIView):
    queryset = Translations.objects.all()
    serializer_class = TranslationsSerializer

class TranslationDetailView(generics.RetrieveAPIView):
    queryset = Translations.objects.all()
    serializer_class = TranslationsSerializer

class FeedInfoListView(generics.ListAPIView):
    queryset = FeedInfo.objects.all()
    serializer_class = FeedInfoSerializer

class FeedInfoDetailView(generics.RetrieveAPIView):
    queryset = FeedInfo.objects.all()
    serializer_class = FeedInfoSerializer

def get_stops(request):
    # データベースから全てのバス停データを取得
    stops = Stops.objects.all()

    # 必要な情報を含むデータをリストに格納
    stops_data = [{'stop_id': stop.stop_id, 'stop_name': stop.stop_name, 'stop_lat': stop.stop_lat, 'stop_lon': stop.stop_lon} for stop in stops]

    # JSON レスポンスを作成
    response_data = {'stops': stops_data}

    # JsonResponseを使ってJSON形式のレスポンスを返す
    response = JsonResponse(response_data)

    response['Access-Control-Allow-Origin'] = 'localhost:3000'

    return response


