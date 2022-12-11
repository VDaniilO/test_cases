from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import HttpResponse

from .serializers import *
from .models import *


class OrdersView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        photo = PhotoModel.objects.all()
        serializer = PhotoSerializers(photo, many=True)
        return Response({'photo': serializer.data})

    def post(self, request):
        photo = PhotoModel.objects.all()
        serializer = PhotoSerializers(photo, many=True)
        return Response({'photo': serializer.data})


# class PhotoView(APIView):
#     def get(self, request, str_name, format=None):
#         photo = PhotoModel.objects.filter(people_on_photo=str_name).all()
#         serializer = PhotoSerializers(photo, many=True)
#         return Response({'photo': serializer.data})


def sort_by(sort_name: str) -> list:
    """
    function for data sort by label on data base
    """
    latest_question_list = PhotoModel.objects.order_by(f'{sort_name}')
    output = '<br>'.join([str(q) for q in latest_question_list])
    return HttpResponse(output)


def all_photo(request):
    latest_question_list = PhotoModel.objects.all()
    output = '<br>'.join([q.photo.url for q in latest_question_list])
    return HttpResponse(output)


def data_sort(request):
    return sort_by('created_at')


def geo_sort(request):
    return sort_by('geo_locate')


def people_sort(request):
    return sort_by('people_on_photo')


def get_id(request, id_num):
    output = get_object_or_404(PhotoModel, pk=id_num)
    return HttpResponse(output)
