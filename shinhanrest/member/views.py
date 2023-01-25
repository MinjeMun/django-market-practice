# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.contrib.auth.hashers import make_password
# from rest_framework import status
from rest_framework import mixins, generics

# from .models import Member
from .serializers import MemberSerializer

# Create your views here.

class MemberRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
): 
    serializer_class = MemberSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)




# ========= API View =========
# class MemberRegisterView(APIView):

#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = make_password(request.data.get('password'))
#         tel = request.data.get('tel')
        
#         # 유효성 검사 기능
#         if Member.objects.filter(username=username).exists():
#             return Response({
#                 'detial':'Already used'
#             }, status=status.HTTP_400_BAD_REQUEST)

#         member = Member (
#             username = username,
#             password = password,
#             tel = tel
#         )
#         member.save()

#         return Response(status=status.HTTP_201_CREATED)
