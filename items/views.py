from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import views
from rest_framework import viewsets


from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer
from .my_generic import MyGenericListCreateView, MyGenericRetriveUpdataDestroyView


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    """
    Category create and list view
    :param Limit: int
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


@api_view(http_method_names=['GET', 'POST'])
def item_list_create_api_view(request):
    # print(request.query_params)
    # print(request.data)
    # data = [
    #     {
    #         "name": "Codify",
    #         "address": "7 mkr"
    #     }
    # ]
    if request.method == 'GET':
        query_set = Item.objects.all()
        serializer = ItemSerializer(query_set, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def item_retrieve_updata_destroy_api_view(request, pk):

    item = get_object_or_404(Item, pk=pk)
    # try:
    #     item = Item.objects.get(pk=pk)
    # except Item.DoesNotExist:
    #     return Response({'detail':'no objects'}, status=404)

    if request.method == 'GET':
        serializer = ItemSerializer(instance=item)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ItemSerializer(instance=item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        item.delete()
        return Response(status=204)


class ItemListCreateView(MyGenericListCreateView):

    # def get(self, request, *args, **kwargs):
    #     query_set = Item.objects.all()
    #     serializer = ItemSerializer(query_set, many=True)
    #     return Response(serializer.data)
    #
    #
    # def post(self, request, *args, **kwargs):
    #     serializer = ItemSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     else:
    #         return Response(serializer.errors, status=400)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemRetrieveUpdataDestroyView(MyGenericRetriveUpdataDestroyView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # def get_object(self, pk):
    #     return get_object_or_404(Item, pk=pk)
    #
    # def get(self, request, pk, *args, **kwargs):
    #     serializer = ItemSerializer(instance=self.get_object(pk))
    #     return Response(serializer.data)
    #
    # def put(self, request, pk, *args, **kwargs):
    #     serializer = ItemSerializer(instance=self.get_object(pk), data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=400)
    #
    # def delete(self, request, pk, *args, **kwargs):
    #     self.get_object(pk).delete()
    #     return Response(status=204)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

