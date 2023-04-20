from django.shortcuts import render

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView
from rest_framework import status
from .serializers import TagSerializer,WriteCommentSerializer,ReplySerializer
from .models import Tag,Comment,Reply
from Account.models import User
# Create your views here.

class TagList(ListCreateAPIView):
    queryset=Tag.objects.all()
    serializer_class=TagSerializer
    paginate_by = 5


class Commentdetail(APIView):
    
    serializer_class=WriteCommentSerializer
    
    def post(self,request):
            comment=Comment(writer_id =request.user.id)
            # all_tag=Tag.objects.values_list('id',flat=True)
            # tags=  request.POST.get('tag',[])
            
            # # for i in range(len(tags)):
            #     if i in all_tag:
            #         tag_obj=get_object_or_404(Tag,id=i)
            #         comment.tag.add(tag_obj)
            # if  "tag" in request.data:
                # request.data.pop("tag")
            serializer=WriteCommentSerializer(comment,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response("comment posted!",status=status.HTTP_200_OK)
    
 
class RetrieveUpdateCommentForReply(APIView):
 
    def put(self,request,pk):
        
        try: 
            get_comment=Comment.objects.get(pk=pk,is_replied=False)
            if request.user.id == get_comment.hotel.manager.id:
                pass
            else:
                 return Response("you can not reply this comment!",status=status.HTTP_400_BAD_REQUEST)
                
        except :
            return Response("comment not found or comment replied!",status=status.HTTP_400_BAD_REQUEST)
        else:
            new_reply=Reply()
            get_comment.reply=new_reply
            get_comment.is_replied=True
            serializer=ReplySerializer(new_reply,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            get_comment.save()
            return Response("comment posted!",status=status.HTTP_200_OK)
            
        
class GetAllManagerComments(APIView):
    def get(self,request):
        all_comments=Comment.objects.filter(hotel__manager__id=request.user.id , is_replied=False)
        serializer=WriteCommentSerializer(all_comments,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
           
            

