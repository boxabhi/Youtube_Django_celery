
from django.urls import path
from .views import *
urlpatterns = [
    path('' , index , name="index"),
    path('<task_id>' , check_status , name="check_status"),
    
    
    
]
