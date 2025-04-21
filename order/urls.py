from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.PayOrder.as_view(), name='payorder'),
    path('closeorder/', views.CloseOrder.as_view(), name='close_order'),
    path('detail/', views.Detail.as_view(), name='detail'),
]
