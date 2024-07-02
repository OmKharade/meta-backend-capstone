from django.urls import path
from . import views

#import obtain_auth_token view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu_item'),
    path('book/', views.BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='book'),
    path('api-token-auth/', obtain_auth_token),
]