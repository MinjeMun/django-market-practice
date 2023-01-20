from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Product,Comment


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Product
        fields = '__all__' # 리스트로 원하는 field만 작성도 가능

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Comment
        fields = '__all__' # 리스트로 원하는 field만 작성도 가능

class CommentCreateSerializer(serializers.ModelSerializer): 
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        required=False
    )
    
    # def validate(self, attrs):
    #     request = self.context['request']
    #     if request.user.is_authenticated:
    #         attrs['user'] = request.user # attrs - ordered dict
    #     else:
    #         raise ValidationError("member is required")
    #     return attrs
    
    class Meta:
        model  = Comment
        fields = '__all__' # 리스트로 원하는 field만 작성도 가능
        # extra_kwargs = {'user': {'required': False}}
