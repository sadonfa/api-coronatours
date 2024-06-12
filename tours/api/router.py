from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import TokenObtainPairView


from tours.api.views import UserApiViewSets, UserView

router = DefaultRouter()

# register the router
router.register(r'tours', UserApiViewSets, 'tours')

# router_user.register(
#     prefix='users', basename='users', viewset=UserApiViewSets
# )

urlpatterns = [
    path('tours/', include(router.urls)),
    # path('auth/me/', UserView.as_view())
]
