from django.urls import path
from .views import *


urlpatterns = [
    path('api/photo/', OrdersView().as_view()),  # all photo on api format and add for auth user
    path('manager/all_photo', all_photo),  # url for out all photo
    path('manager/data_sort', data_sort),  # url for out all photo sorted by data
    path('manager/geo_sort', geo_sort),  # url for out all photo sorted by locate
    path('manager/people_sort', people_sort),  # url for out all photo sorted by people on photo
    path('manager/<int:id_num>/', get_id),  # url for out photo by id
    # path('<str:str_name>/', PhotoView.as_view()),  # 4 task not ended
]
