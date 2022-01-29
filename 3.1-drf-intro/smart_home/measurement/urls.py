from django.urls import path
from .views import APISensors, APISensorUpdate, APIMeasurements

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', APISensors.as_view()),
    path('sensors/update/<pk>', APISensorUpdate.as_view()),
    path('measurements/', APIMeasurements.as_view()),
]
