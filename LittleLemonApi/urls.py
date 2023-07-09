from django.urls import path
from .views import MenuItemList,GetMenuItem,Manager,ListManager,DeliveryStaffs,AddDeliveryStaff,CartView,OrderView

urlpatterns = [
    path("menu-items",MenuItemList.as_view(),name="list-menu-items"),
    path("menu-items/<int:id>",GetMenuItem.as_view(),name="menu-item"),
    path("groups/manager/users",ListManager.as_view(),name="list-manager"),
    path("groups/manager/users/<int:id>",Manager.as_view(),name="manager"),
    path("groups/delivery-crew/users/",DeliveryStaffs.as_view(),name="list-delivery-crews"),
    path("groups/delivery-crew/users/<int:id>",AddDeliveryStaff.as_view(),name="delivery-staff"),
    path("cart/menu-items",CartView.as_view(),name="cart"),
    path("orders",OrderView.as_view(),name="orders"),
    path("orders/<int:orderId>",OrderView.as_view(),name="order-detail")
  


]