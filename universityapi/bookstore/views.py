from django.shortcuts import render

from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class BookList(APIView):
    def get(self,request):
        books=Book.objects.all()   #complex data type
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    
class BookCreate(APIView):
    def post(self,request):
        serializer=BookSerializer(data=request.data)    
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)


class BookDetails(APIView):
    def get_book_by_pk(self,pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            return Response({
                'error':'Book doesnot exist!!!'
            },status=status.HTTP_400_BAD_REQUEST)

    
    def get(self,request,pk):
        book=self.get_book_by_pk(pk)
        serializer=BookSerializer(book)
        return Response(serializer.data) 

    def put(self,request,pk):
        book=self.get_book_by_pk(pk)
        serializer=BookSerializer(book,data=request.data)    
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        book=self.get_book_by_pk(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


