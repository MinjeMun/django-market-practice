from rest_framework import serializers
from .models import Product, Comment, Like


class ProductSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField() # Create 할 때는 알아서 반영함

    def get_comment_count(self, obj): # self-serialzer, obj-객체
        return obj.comment_set.all().count()
        # return Comment.objects.filter(product=obj).count()

    class Meta:
        model  = Product
        fields = '__all__' # 리스트로 원하는 field만 작성도 가능

class CommentSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    member_username = serializers.SerializerMethodField()
    tstamp = serializers.DateTimeField(
        read_only=True, format='%Y-%m-%d %H:%M%S'
    )

    def get_product_name(self, obj):
        return obj.product.name

    def get_member_username(self, obj):
        return obj.member.username

    class Meta:
        model  = Comment
        fields = '__all__' # 리스트로 원하는 field만 작성도 가능

class CommentCreateSerializer(serializers.ModelSerializer): 
    # 로그인 된 사용자로부터 자동으로 저장하기 위한 설정
    user = serializers.HiddenField( # 숨겨진 값에 대한 default 설정
        default=serializers.CurrentUserDefault(),
        required=False
    )
    
    # validate_필드명 - 해당 필드에 대한 유효성 검사
    def validate_user(self, value): 
        if not value.is_authenticated:
            raise serializers.ValidationError("user is required")
        return value
    
    class Meta:
        model  = Comment
        fields = '__all__' # 리스트로 원하는 field만 작성도 가능
        # extra_kwargs = {'user': {'required': False}}

class LikeCreateSerializer(serializers.ModelSerializer): 
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        required=False
    ) 

    # validate_필드명 - 해당 필드에 대한 유효성 검사
    def validate_user(self, value): 
        if not value.is_authenticated:
            raise serializers.ValidationError("user is required")
        return value
    
    class Meta:
        model  = Like
        fields = '__all__' # 리스트로 원하는 field만 작성도 가능
        # extra_kwargs = {'user': {'required': False}}

