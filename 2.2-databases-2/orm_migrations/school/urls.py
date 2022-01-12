from django.urls import path

import school
from school.views import students_list

urlpatterns = [
    path('', school.views.students_list, name='students'),
]