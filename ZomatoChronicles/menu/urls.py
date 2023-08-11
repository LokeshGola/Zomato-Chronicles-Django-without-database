from django.urls import path
from . import views

urlpatterns = [
    path("menu/", views.menu_list, name="menu_list"),
    path("menu/add/", views.add_dish, name="add_dish"),
    path("menu/update/<str:dish_name>/", views.update_dish, name="update_dish"),
    path("menu/remove/<str:dish_name>/", views.remove_dish, name="remove_dish"),
    path("menu/take_order/", views.take_order, name="take_order"),
    path("menu/order_list/", views.order_list, name="order_list"),
    
    path("menu/update_order_status/<int:order_id>/", views.update_order_status, name="update_order_status"),
    path("menu/review_orders/", views.review_orders, name="review_orders"),
    path("menu/error/", views.error, name="error"),
    path("menu/filter_orders/<str:status>/", views.filter_orders_by_status, name="filter_orders"),
    path("", views.homepage, name="homepage"),


]
