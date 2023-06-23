from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.product_detail, name='product_detail_url')
]