from rest_framework import viewsets, generics
from sales_network.models import Link, Product
from sales_network.serializers import LinkSerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(viewsets.ModelViewSet):
    """ Viewset для создания, отображения, редакирования, удаления сущности "Product". """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class LinkCreateAPIView(generics.CreateAPIView):
    """ Класс-контроллер для создания сущности "Звено". """
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated]


class LinkListAPIView(generics.ListAPIView):
    """ Класс-контроллер для отображения всех сущностей "Звено". """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_fields = ['country', ]


class LinkRetrieveView(generics.RetrieveAPIView):
    """ Класс-контроллер для отображения одной сущности "Звено". """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated]


class LinkUpdateView(generics.UpdateAPIView):
    """ Класс-контроллер для редактирования сущности "Звено". """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated]


class LinkDestroyView(generics.DestroyAPIView):
    """ Класс-контроллер для удаления сущности "Звено". """
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated]
