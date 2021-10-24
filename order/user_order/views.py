from rest_framework import viewsets, status
from .models import Shop, Order
from .serializers import ShopSerializer, OrderSerializer

from rest_framework.response import Response

from .producer import publish

class ShopViewSet(viewsets.ViewSet):
  def list(self, requeset):   #/api/shop
    shops = Shop.objects.all()
    serializer = ShopSerializer(shops, many=True)
    publish()
    return Response(serializer.data)

  def create(self, requeset):   #/api/shop
    serializer = ShopSerializer(data=requeset.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

  def retrieve(self, requeset, pk=None):   #/api/shop/<str:idx>
    shop = Shop.objects.get(id=pk)
    serrializer = ShopSerializer(shop)
    return Response(serrializer.data)

  def update(self, requeset, pk=None):   #/api/shop/<str:idx>
    shop = Shop.objects.get(id=pk)
    serializer = ShopSerializer(instance = shop, data=requeset.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

  def destroy(self, requeset, pk=None):   #/api/shop/<str:idx>
    shop = Shop.objects.get(id=pk)
    shop.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class OrderViewSet(viewsets.ViewSet):
  def list(self, requeset):   #/api/order
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

  def create(self, requeset):   #/api/order
    serializer = OrderSerializer(data=requeset.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

  def retrieve(self, requeset, pk=None):   #/api/order/<str:idx>
    order = Order.objects.get(id=pk)
    serrializer = OrderSerializer(order)
    return Response(serrializer.data)

  def update(self, requeset, pk=None):   #/api/order/<str:idx>
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(instance = order, data=requeset.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

  def destroy(self, requeset, pk=None):   #/api/order/<str:idx>
    order = Order.objects.get(id=pk)
    order.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)