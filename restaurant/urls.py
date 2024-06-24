from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tables', views.BookingViewSet, basename = 'tables')

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', include(router.urls)),
    path('booking/', include(router.urls), name = "booking"),
    path('menu/', views.MenuView.as_view(), name = "menu"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name = "single_menu_item"),
    path('api-token-auth', view = obtain_auth_token),
]