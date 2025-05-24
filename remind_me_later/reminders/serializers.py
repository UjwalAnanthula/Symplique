from rest_framework import serializers
from datetime import datetime, date
from .models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ['id', 'delivery_date', 'delivery_time', 'delivery_method', 'message']

    def validate_message(self, value):
        if len(value) > 500:
            raise serializers.ValidationError("Message cannot exceed 500 characters.")
        if not value.strip():
            raise serializers.ValidationError("Message cannot be empty.")
        return value

    def validate(self, data):
        delivery_date = data.get('delivery_date')
        delivery_time = data.get('delivery_time')
        current_time = datetime.now().time()
        current_date = date.today()

        if delivery_date < current_date:
            raise serializers.ValidationError({"delivery_date": "Date cannot be in the past."})

        if delivery_date == current_date and delivery_time <= current_time:
            raise serializers.ValidationError({"delivery_time": "Time must be in the future for today's date."})

        return data
