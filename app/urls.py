from rest_framework.routers import DefaultRouter

from .views import (DriverViewSet, DishViewSet, DeliveryViewSet, CustomerViewSet,
                    OrderViewSet, MenuViewSet, PaymentViewSet)


router = DefaultRouter()

router.register('driver', DriverViewSet)
router.register('dish', DishViewSet)
router.register('delivery', DeliveryViewSet)
router.register('customer', CustomerViewSet)
router.register('order', OrderViewSet)
router.register('menu', MenuViewSet)
router.register('payment', PaymentViewSet)

urlpatterns = router.urls