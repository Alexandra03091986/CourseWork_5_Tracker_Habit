from rest_framework.serializers import ModelSerializer

from habits.models import Habit


class HabitSerializer(ModelSerializer):
    """Сериализатор для объектов привычек."""
    class Meta:
        model = Habit
        fields = '__all__'


class PublicHabitSerializer(ModelSerializer):
    """Сериализатор для публичных привычек"""
    class Meta:
        model = Habit
        fields = ("action", "pleasant_habit", "time_execution")
