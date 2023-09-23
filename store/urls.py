
from django.urls import path
from .views import AddStoreStatus
from .views import AddStoreBusinessHours
from .views import AddStoreTimeZone


urlpatterns = [
    path('addStore', AddStoreStatus.as_view()),
    path('addBusinessTime', AddStoreBusinessHours.as_view()),
    path('addTimeZone', AddStoreTimeZone.as_view())

]
