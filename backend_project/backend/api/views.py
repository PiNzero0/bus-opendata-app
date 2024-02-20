# views.py
from rest_framework import generics
from .models import *
from .serializers import *
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
import asyncio
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime ,timezone
from zoneinfo import ZoneInfo
from django.utils import timezone


# modles.pyを参照して、クラスを作成する
class AgencyListView(generics.ListAPIView):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer

class AgencyDetailView(generics.RetrieveAPIView):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer

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
"""
class TranslationListView(generics.ListAPIView):
    queryset = Translations.objects.all()
    serializer_class = TranslationsSerializer

class TranslationDetailView(generics.RetrieveAPIView):
    queryset = Translations.objects.all()
    serializer_class = TranslationsSerializer
"""
class FeedInfoListView(generics.ListAPIView):
    queryset = Feed_Info.objects.all()
    serializer_class = FeedInfoSerializer

class FeedInfoDetailView(generics.RetrieveAPIView):
    queryset = Feed_Info.objects.all()
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

    return response

@api_view(['GET'])
def get_stop_details(request, stop_id):
    try:
        stop_times = Stop_Times.objects.filter(stop_id=stop_id).distinct('trip_id')
        serializer = Stop_TimesSerializer(stop_times, many=True)
        trip_ids = [stop_time['trip_id'] for stop_time in serializer.data]
        return Response(trip_ids)
    except Stop_Times.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

#route_idに紐づくroute_short_nameとroute_long_nameを取得する
@api_view(['GET'])
def get_route_short_name(request, route_id):
    try:
        route = Routes.objects.get(route_id=route_id)
        serializer = RoutesSerializer(route)
        return Response(serializer.data)
    except Routes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

"""
@api_view(['GET'])
#バスの運行状況を取得する。（2024年1月22日の運行状況を取得する）

def get_bus_info(request, stop_id):
    try:

        # 固定の日付（2024年1月22日）を使用
        fixed_date = datetime(2024, 1, 22, tzinfo=ZoneInfo("Asia/Tokyo"))
        today = fixed_date.strftime('%Y-%m-%d')
        stop_times = Stop_Times.objects.filter(stop_id=stop_id).distinct('trip_id')

        result_data = []  # 結果データを格納するリスト

        for stop_time in stop_times:
            trips = Trips.objects.filter(trip_id=stop_time.trip_id)
            serializer = TripsSerializer(trips, many=True)
            for trip in serializer.data:
                service_id = trip['service_id']
                route_id = trip['route_id']
                direction_id = trip['direction_id']

                try:
                    # Calendar_Datesからデータを取得
                    calendar_dates = Calendar_Dates.objects.get(service_id=service_id, date=today)

                    stop_times_data = Stop_Times.objects.filter(stop_id=stop_id, trip_id=stop_time.trip_id)
                    serializer_stop_times = Stop_TimesSerializer(stop_times_data, many=True)
                    
                    # 到着時間と出発時間を抽出
                    times_data = [{'arrival_time': stop_time['arrival_time'], 'departure_time': stop_time['departure_time']}
                                  for stop_time in serializer_stop_times.data]

                    # 一つずつtimes_dataをresult_dataに追加
                    for time_data in times_data:
                        result_data.append({'source': 'calendar_dates', 'route_id': route_id, 'direction_id': direction_id, **time_data})
                except Calendar_Dates.DoesNotExist:
                    # Calendar_Datesが存在せず、Calendarが存在する場合に取得
                    try:
                        calendar = Calendar.objects.get(service_id=service_id)
                        if is_weekday_today(calendar, today):
                            stop_times_data = Stop_Times.objects.filter(stop_id=stop_id, trip_id=stop_time.trip_id)
                            serializer_stop_times = Stop_TimesSerializer(stop_times_data, many=True)

                            # 到着時間と出発時間を抽出
                            times_data = [{'arrival_time': stop_time['arrival_time'], 'departure_time': stop_time['departure_time']}
                                          for stop_time in serializer_stop_times.data]

                            # 一つずつtimes_dataをresult_dataに追加
                            for time_data in times_data:
                                result_data.append({'source': 'calendar', 'route_id': route_id, 'direction_id': direction_id, **time_data})
                    except Calendar.DoesNotExist:
                        pass

        return Response({'data': result_data})
    except Stop_Times.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
"""
@api_view(['GET'])
#バスの運行状況を取得する。（2024年1月21日の運行状況を取得する）

def get_bus_info(request, stop_id):
    try:

        # 固定の日付（2024年1月21日）を使用
        fixed_date = datetime(2024, 1, 21, tzinfo=ZoneInfo("Asia/Tokyo"))
        today = fixed_date.strftime('%Y-%m-%d')
        stop_times = Stop_Times.objects.filter(stop_id=stop_id).distinct('trip_id')

        result_data = []  # 結果データを格納するリスト

        for stop_time in stop_times:
            trips = Trips.objects.filter(trip_id=stop_time.trip_id)
            serializer = TripsSerializer(trips, many=True)
            for trip in serializer.data:
                service_id = trip['service_id']
                route_id = trip['route_id']
                direction_id = trip['direction_id']

                try:
                    # Calendar_Datesからデータを取得
                    calendar_dates = Calendar_Dates.objects.get(service_id=service_id, date=today)

                    stop_times_data = Stop_Times.objects.filter(stop_id=stop_id, trip_id=stop_time.trip_id)
                    serializer_stop_times = Stop_TimesSerializer(stop_times_data, many=True)
                    
                    # 到着時間と出発時間を抽出
                    times_data = [{'arrival_time': stop_time['arrival_time'], 'departure_time': stop_time['departure_time']}
                                  for stop_time in serializer_stop_times.data]

                    # 一つずつtimes_dataをresult_dataに追加
                    for time_data in times_data:
                        result_data.append({'source': 'calendar_dates', 'route_id': route_id, 'direction_id': direction_id, **time_data})
                except Calendar_Dates.DoesNotExist:
                    # Calendar_Datesが存在せず、Calendarが存在する場合に取得
                    try:
                        calendar = Calendar.objects.get(service_id=service_id)
                        if is_weekday_today(calendar, today):
                            stop_times_data = Stop_Times.objects.filter(stop_id=stop_id, trip_id=stop_time.trip_id)
                            serializer_stop_times = Stop_TimesSerializer(stop_times_data, many=True)

                            # 到着時間と出発時間を抽出
                            times_data = [{'arrival_time': stop_time['arrival_time'], 'departure_time': stop_time['departure_time']}
                                          for stop_time in serializer_stop_times.data]

                            # 一つずつtimes_dataをresult_dataに追加
                            for time_data in times_data:
                                result_data.append({'source': 'calendar', 'route_id': route_id, 'direction_id': direction_id, **time_data})
                    except Calendar.DoesNotExist:
                        pass

        return Response({'data': result_data})
    except Stop_Times.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


"""
# バスの運行状況を取得する。
@api_view(['GET'])
def get_bus_info(request, stop_id):
    try:
        today = datetime.now(ZoneInfo("Asia/Tokyo")).strftime('%Y-%m-%d')
        stop_times = Stop_Times.objects.filter(stop_id=stop_id).distinct('trip_id')

        result_data = []  # 結果データを格納するリスト

        for stop_time in stop_times:
            trips = Trips.objects.filter(trip_id=stop_time.trip_id)
            serializer = TripsSerializer(trips, many=True)
            for trip in serializer.data:
                service_id = trip['service_id']
                route_id = trip['route_id']
                direction_id = trip['direction_id']

                try:
                    # Calendar_Datesからデータを取得
                    calendar_dates = Calendar_Dates.objects.get(service_id=service_id, date=today)

                    stop_times_data = Stop_Times.objects.filter(stop_id=stop_id, trip_id=stop_time.trip_id)
                    serializer_stop_times = Stop_TimesSerializer(stop_times_data, many=True)
                    
                    # 到着時間と出発時間を抽出
                    times_data = [{'arrival_time': stop_time['arrival_time'], 'departure_time': stop_time['departure_time']}
                                  for stop_time in serializer_stop_times.data]

                    # 一つずつtimes_dataをresult_dataに追加
                    for time_data in times_data:
                        result_data.append({'source': 'calendar_dates', 'route_id': route_id, 'direction_id': direction_id, **time_data})
                except Calendar_Dates.DoesNotExist:
                    # Calendar_Datesが存在せず、Calendarが存在する場合に取得
                    try:
                        calendar = Calendar.objects.get(service_id=service_id)
                        if is_weekday_today(calendar, today):
                            stop_times_data = Stop_Times.objects.filter(stop_id=stop_id, trip_id=stop_time.trip_id)
                            serializer_stop_times = Stop_TimesSerializer(stop_times_data, many=True)

                            # 到着時間と出発時間を抽出
                            times_data = [{'arrival_time': stop_time['arrival_time'], 'departure_time': stop_time['departure_time']}
                                          for stop_time in serializer_stop_times.data]

                            # 一つずつtimes_dataをresult_dataに追加
                            for time_data in times_data:
                                result_data.append({'source': 'calendar', 'route_id': route_id, 'direction_id': direction_id, **time_data})
                    except Calendar.DoesNotExist:
                        pass

        return Response({'data': result_data})
    except Stop_Times.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
"""
def is_weekday_today(calendar, today):
    today_datetime = datetime.strptime(today, '%Y-%m-%d')
    today_weekday = today_datetime.weekday()
    return getattr(calendar, _get_weekday_field_name(today_weekday)) == 1

def _get_weekday_field_name(weekday):
    return ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'][weekday]

#route_idに紐づくstop_idを取得する
@api_view(['GET'])
def get_stop_id(request, route_id):
    try:
        # 与えられた route_id に対応するすべての trip_id を取得
        trip_ids = Trips.objects.filter(route_id=route_id).values_list('trip_id', flat=True)

        # trip_id ごとに対応する stop_id を取得
        stop_ids = set()
        for trip_id in trip_ids:
            stops = Stop_Times.objects.filter(trip_id=trip_id).values_list('stop_id', flat=True)
            stop_ids.update(stops)

        # 取得した stop_id に対応する停留所情報を取得
        stops_info = []
        for stop_id in stop_ids:
            stop = Stops.objects.get(stop_id=stop_id)
            stops_info.append({
                "stop_id": stop.stop_id,
                "stop_name": stop.stop_name,
                "stop_lat": stop.stop_lat,
                "stop_lon": stop.stop_lon
            })

        # JSON レスポンスを構築
        response_data = {"stops": stops_info}
        return JsonResponse(response_data, safe=False)
    except Trips.DoesNotExist:
        return JsonResponse({"error": "Route not found"}, status=404)
    except Stop_Times.DoesNotExist:
        return JsonResponse({"error": "Stop times not found"}, status=404)
    except Stops.DoesNotExist:
        return JsonResponse({"error": "Stop not found"}, status=404)

@api_view(['GET'])
def get_pokemon_data(request, name):
    pokemon_data = {
        'akita': {'name': 'ポケふた秋田', 'img': './img/poke-akita.png', 'lat': 39.752642, 'lng': 140.061295},
        'oga': {'name': 'ポケふた男鹿', 'img': './img/poke-akita.png', 'lat': 39.88201, 'lng': 140.84772},
        'yokote': {'name': 'ポケふた横手', 'img': './img/poke-akita.png', 'lat': 39.293561, 'lng': 140.545941},
        'semboku': {'name': 'ポケふた仙北', 'img': './img/poke-akita.png', 'lat': 39.699992, 'lng': 140.662631},
        'kaduno': {'name': 'ポケふた鹿角', 'img': './img/poke-akita.png', 'lat': 40.181213, 'lng': 140.785474},
    }

    if img in pokemon_data:
        return Response(pokemon_data[img])
    else:
        return Response({'error': 'Invalid img parameter'}, status=400)
