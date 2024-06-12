from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import TokenObtainPairView


from tours.views import TourApiViewSets


router = DefaultRouter()

# register the router
router.register(r'tours', TourApiViewSets, 'tours')

urlpatterns = [
    path('tours/', include(router.urls)),
]
