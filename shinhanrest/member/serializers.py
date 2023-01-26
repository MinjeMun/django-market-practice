from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Member

class MemberSerializer(serializers.ModelSerializer):

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Too short')
        # 유효성 검사가 끝난 값을 반환
        return make_password(value)



    # 비밀번호 일치 여부를 백엔드에서 처리할 경우

    # password_check = serializers.CharField()

    # def validate(self, attrs):
    #     if len(attrs['password']) < 8:
    #         raise serializers.ValidationError('Too short password')

    #     if attrs['password'] != attrs['password_check']:
    #         raise serializers.ValidationError('비밀번호 일치하지 않음')

    #     attrs['password'] = make_password(attrs['password'])

    class Meta:
        model = Member
        fields = ('id','username','tel','password',)
        extra_kwargs = {
            'id': {
                'read_only': True,
            },
            'password': { 
                'write_only': True, # 쓸때만 불러오기 나머지는 불러오기 x
            },
        }

        