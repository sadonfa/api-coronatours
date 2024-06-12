from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response

from tours.models import Tours
from tours.serializers import ToursSerializers


class TourApiViewSets(ModelViewSet):
    serializer_class = ToursSerializers
    queryset = Tours.objects.all()


# class UserView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         serializer = ToursSerializers(request.user)
#         return Response(serializer.data)
