from django.urls import path
from .views import MenuItemList,MenuItemDetail,Manager,ListManager,DeliveryStaffs,AddDeliveryStaff,CartView,OrderView

urlpatterns = [
    path("menu-items",MenuItemList.as_view(),name="list-menu-items"),
    path("menu-items/<int:pk>",MenuItemDetail.as_view(),name="menu-item"),
    path("groups/manager/users",ListManager.as_view(),name="list-manager"),
    path("groups/manager/users/<int:pk>",Manager.as_view(),name="manager"),
    path("groups/delivery-crew/users/",DeliveryStaffs.as_view(),name="list-delivery-crews"),
    path("groups/delivery-crew/users/<int:pk>",AddDeliveryStaff.as_view(),name="delivery-staff"),
    path("cart/menu-items",CartView.as_view(),name="cart"),
    path("orders",OrderView.as_view(),name="orders"),
    path("orders/<int:pk>",OrderView.as_view(),name="order-detail")
  


]