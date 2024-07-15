from django.urls import path
from sales_network.apps import SalesNetworkConfig
from sales_network.views import LinkListAPIView, LinkCreateAPIView, LinkDestroyView, LinkRetrieveView, LinkUpdateView, \
    ProductViewSet
from rest_framework.routers import DefaultRouter

app_name = SalesNetworkConfig.name

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
                  path('network/create/', LinkCreateAPIView.as_view(), name='link-create'),
                  path('network/list/', LinkListAPIView.as_view(), name='link-list'),
                  path('network/<int:pk>/', LinkRetrieveView.as_view(), name='link-get'),
                  path('network/update/<int:pk>/', LinkUpdateView.as_view(), name='link-update'),
                  path('network/delete/<int:pk>/', LinkDestroyView.as_view(), name='link-delete'),
              ] + router.urls
