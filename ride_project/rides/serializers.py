from rest_framework import serializers
from .models import Ride

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ('rider', 'driver', 'pickup_location', 'dropoff_location', 'status', 'created_at', 'updated_at')

    class RideSerializer(serializers.ModelSerializer):
        class Meta:
            model = Ride
            fields = ('rider', 'driver', 'pickup_location', 'dropoff_location', 'status', 'created_at', 'updated_at')

        def update(self, instance, validated_data):
            if 'status' in validated_data:
                status = validated_data['status']
                if status == 'Started':
                    instance.start_ride()
                elif status == 'Completed':
                    instance.complete_ride()
                elif status == 'Cancelled':
                    instance.cancel_ride()
            return instance