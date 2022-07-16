from rest_framework import status
from rest_framework.response import Response
from .models import users
from .serializer import *
from rest_framework.views import APIView
from django.http import Http404
from django.core.paginator import Paginator
from operator import itemgetter
from django.db.models import Q
from rest_framework import generics
# Create your views here.

class user(APIView):
    
    def get(self,request):
        page = request.query_params.get('page',1)
        limit = request.query_params.get('limit',5)
        name = request.query_params.get('name','')
        sort = request.query_params.get('sort','')
        
        if name:
            use = users.objects.distinct().filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))
        else:
            use = users.objects.all()
        
        page_object = Paginator(use,limit)
        if page == 'last':
            page = page_object.num_pages
        page_use = page_object.get_page(page)
        if sort :
            try:
                if sort[0] == '-':
                    page_use = sorted(page_use.object_list.values(),key=itemgetter(sort[1:len(sort)]),reverse=True)
                else:
                    page_use = sorted(page_use.object_list.values(),key=itemgetter(sort))
            except:
                raise Http404
        serializer = usersSerializer(page_use,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = usersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)    
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class userid(generics.RetrieveUpdateDestroyAPIView):
    queryset = users.objects.all()
    lookup_field = 'pk'
    serializer_class = usersidSerializer
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = usersSerializer(queryset)
        return Response(serializer.data)        

