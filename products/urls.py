from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<category_type>', views.product_list, name='product_list'),
    path('product/<int:pk>', views.product_details, name='product'),
]