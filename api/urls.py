from django.urls import path, include
from .views import *

urlpatterns = [
    path('user/', user),
    path('user/<int:pk>/', user),
    path('project/', project),
    path('project/<int:pk>/', project),
    path('task/', task),
    path('task/<int:pk>/', task),

    path('auth/', include('dj_rest_auth.urls'))
]