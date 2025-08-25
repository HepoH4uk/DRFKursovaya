from rest_framework import serializers

from .models import Habit
from .validators import HabitValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
        }
        validators = [HabitValidator()]


class HabitPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        exclude = ('place',)
