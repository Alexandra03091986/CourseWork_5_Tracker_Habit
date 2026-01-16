from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from habits.models import Habit
from habits.serializers import HabitSerializer, PublicHabitSerializer


class HabitCreateAPIView(CreateAPIView):
    """Контроллер создания привычки."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # permission_classes = ()   # временно


class HabitListAPIView(ListAPIView):
    """Контроллер получения списка всех своих привычек."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # permission_classes = []   # временно
#     еще дописать фильтры возможно


class HabitRetrieveAPIView(RetrieveAPIView):
    """Контроллер получения информации о конкретной привычке."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # permission_classes = []   # временно


class HabitUpdateAPIView(UpdateAPIView):
    """Контроллер обновления информации о привычке."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # permission_classes = []   # временно


class HabitDestroyAPIView(DestroyAPIView):
    """Контроллер удаления привычки."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # permission_classes = []   # временно


class PublicHabitListAPIView(ListAPIView):
    """ Контроллер получения списка всех публичных привычек."""
    queryset = Habit.objects.filter(is_published=True)
    serializer_class = PublicHabitSerializer
    # permission_classes = []   # временно
