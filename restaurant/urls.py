from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', include(router.urls)),
    path('booking/', include(router.urls)),
    path('menu/', views.MenuView.as_view(), name = "menu_items"),
    path('menu/<int: pk', views.SingleMenuItemView.as_view(), name = "single_menu_item"),
]