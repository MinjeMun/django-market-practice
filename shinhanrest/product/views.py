from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Product, Comment, Like
from .serializers import (
    ProductSerializer, 
    CommentSerializer, 
    CommentCreateSerializer,
    LikeCreateSerializer
    )
from.paginations import ProductLargePagination

# 상속을 여러개 받음 (부모-자식이랑은 좀 다른 관계)

class ProductListView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,     
    generics.GenericAPIView
): 
    serializer_class = ProductSerializer
    pagination_class = ProductLargePagination
    # permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        # prefetch_related로 필요한 값을 미리 불러옴 (시간 단축 -. 성능 개선)
        products = Product.objects.all().prefetch_related('comment_set') 

        # if self.request.user.is_authenticated: # 로그인 검사
        #     products = Product.objects.all()
        # else:
        #     products = Product.objects.none()
        
        name = self.request.query_params.get('name')

        if name:
            products = products.filter(name__contains=name)
        
        return products.order_by('id')


    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class ProductDetailView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView
):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, args, kwargs)

class CommentListView(
    mixins.ListModelMixin,    
    generics.GenericAPIView
): 
    serializer_class = CommentSerializer

    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        if product_id:
                return Comment.objects \
                                    .filter(product_id=product_id) \
                                    .select_related('member','product') \
                                    .order_by('-id')
        return Comment.objects.none()

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)


class CommentCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = CommentCreateSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)


class LikeCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = LikeCreateSerializer

    def get_queryset(self):
        return Like.objects.all()

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        if Like.objects.filter(user=request.user, product_id=product_id).exists(): # id 없으면 만들고
            Like.objects.filter(user=request.user, product_id=product_id).delete() # id 있으면 지우고
            return Response(status=status.HTTP_204_NO_CONTENT)

        return self.create(request, args, kwargs)