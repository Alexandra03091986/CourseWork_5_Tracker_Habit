from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitDestroyAPIView, \
    HabitUpdateAPIView, PublicHabitListAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path("habit/", HabitListAPIView.as_view(), name="habit_list"),
    path("habit/create/", HabitCreateAPIView.as_view(), name="breeds_create"),
    path("habit/<int:pk>/", HabitRetrieveAPIView.as_view(), name="breeds_retrieve"),
    path("habit/<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("habit/<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habit_delete"),
    path("public/", PublicHabitListAPIView.as_view(), name="public"),
]
