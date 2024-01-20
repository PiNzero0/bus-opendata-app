from rest_framework import serializers
from .models import *
# models.pyを参照して、クラスを作成する
class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = '__all__'

class AgencyjpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency_jp
        fields = '__all__'

class StopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stops
        fields = '__all__'

class Stop_TimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop_Times
        fields = '__all__'

class RoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = '__all__'

class Route_jpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes_jp
        fields = '__all__'

class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = '__all__'

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = '__all__'

class CalendarDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar_Dates
        fields = '__all__'

class FareAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fare_Attributes
        fields = '__all__'

class FareRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fare_Rules
        fields = '__all__'

class ShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shapes
        fields = '__all__'

class FrequencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Frequencies
        fields = '__all__'

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfers
        fields = '__all__'

"""class TranslationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translations
        fields = '__all__'"""

class FeedInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed_Info
        fields = '__all__'